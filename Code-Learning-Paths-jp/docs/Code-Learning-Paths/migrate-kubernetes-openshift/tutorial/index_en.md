---
authors: ''
completed_date: '2021-08-23'
components:
- openshift
- kubernetes
- devops
draft: false
excerpt: This tutorial walks you through moving workloads from Kubernetes to OpenShift,
  with a focus on changing images and migrating security policies.
menu_order: 4
meta_description: This tutorial walks you through moving workloads from Kubernetes
  to OpenShift, with a focus on changing images and migrating security policies.
meta_keywords: migrate Kubernetes to OpenShift, openshift migration, SCCs
meta_title: 'Migrate your workloads from Kubernetes to OpenShift: Image and PSP migration'
primary_tag: containers
subtitle: Tutorial showing sample migration from Kubernetes to OpenShift
title: Tutorial example
---

The previous parts of this learning path highlighted the two areas where you need to focus when migrating your workloads from Kubernetes to OpenShift. As a reminder, you need to carefully consider how to:

- Update your images to make them run on both Kubernetes and OpenShift
- Migrate your Kubernetes Pod Security Policies (PSP) to OpenShift Security Context Constraints (SCC)

This tutorial walks you through moving workloads from Kubernetes to OpenShift, with a focus on changing images and migrating security policies.

## Migration scenario

The application used in this tutorial is a simple Node.js application which exposes certain APIs and records the statistics of those APIs. The statistics of the APIs are saved as a .CSV file that contains the API name and number of times it was called. This tutorial uses a directory of container file system as its volume reference, but you can replace the file system with [persistent volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

You will deploy the sample application on a Kubernetes cluster which has pod security policies (PSPs) with the following capabilities:

* Specific users can access the application container
* Allows access to` EmptyDir` volume
* Restricts privileged access to users

This tutorial walks you through how to migrate the sample application from Kubernetes to OpenShift while following the best practices for container images and retaining the security policies to deploy applications.

## Pre-requisites

To complete the steps in this tutorial, you should have access to:

* [IBM Cloud account](https://cloud.ibm.com), if you are trying this tutorial on IBM Cloud
* [Kubernetes cluster](https://cloud.ibm.com/kubernetes/catalog/create). This tutorial uses the IBM Kubernetes Service which you can access in the IBM cloud catalog
* [An OpenShift cluster](https://cloud.ibm.com/kubernetes/catalog/create?platformType=openshift). This tutorial uses an OpenShift cluster on IBM Cloud. You should be able to replicate the steps in other OpenShift environments as well.
* [Git client](https://git-scm.com/downloads)
* [kubectl client](https://kubernetes.io/docs/tasks/tools/)
* [oc client](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html)
* [DockerHub account](https://hub.docker.com/)

## Estimated time

It should take you approximately 60 minutes to complete this tutorial.

## Steps

1. Get the code
2. Deploy your application to Kubernetes
3. Prepare code for migration
4. Deploy the migrated application to OpenShift
5. Analyze the results

### 1. Get the code

Clone the following repository.

```
git clone https://github.com/IBM/migrate-apps-from-k8s-to-ocp
```

### 2. Deploy your application to Kubernetes

**1. Build your container image**

First, you need to build the container image of your application. This tutorial uses DockerHub as its image registry. You may choose any image registry of your choice.

Execute the following commands to build the container image:

```
cd migrate-apps-from-k8s-to-ocp/deploy-to-k8s/
cp -pr ../app .
# docker build -t <your-docker-account>/<image-name> .
docker build -t <your-docker-account>/k8image .
docker push <your-docker-account>/k8image
```
Make a note of your image URL `<your-docker-account>/k8image`. Modify `deploy.yaml` using the following command:

```
sed -i '' s#IMAGE#<your-docker-account>/k8image# deploy.yaml
```

**2. Deploy the application**

Log in to your Kubernetes cluster using a terminal window.

For IBM Cloud Kubernetes service, navigate to Clusters under Resource Summary section on IBM Cloud dashboard, then click on the name of your cluster. Select `Actions > Connect via CLI` and execute the steps provided to access the cluster.

This tutorial uses namespace `mlp-ns` and service account `mlp-sa`. Go ahead and create the namespace and service account .

```
kubectl create namespace mlp-ns
kubectl create serviceaccount mlp-sa -n mlp-ns
```

Navigate to the `deploy-to-k8s` folder of your cloned repository on a terminal window and execute the commands as given below.

```
cd migrate-apps-from-k8s-to-ocp/deploy-to-k8s

## Deploy pod security policy using the file `psp.yaml`
kubectl apply -f psp.yaml

## Deploy rbac using the file `rbac.yaml`
kubectl apply -f rbac.yaml -n mlp-ns

## Deploy the application using the deployment file `deploy.yaml`
kubectl apply -f deploy.yaml -n mlp-ns

## Verify that the application is deployed fine
kubectl get pods -n mlp-ns
```

Use the following command to verify if the correct PSP is applied to the pod.

```
kubectl get pod <pod_name> -o yaml -n mlp-ns | grep psp
```

It should show the output as:

```
kubernetes.io/psp: custom-mlp-psp
```

Notice that `custom-mlp-psp` PSP is applied for the pod deployment.


**3. Access the application**

You can get the public IP of your IBM Kubernetes cluster using the command `kubectl get nodes -o wide` and access the application using `http://<cluster-public-ip>:32600/`.

It exposes three APIs: `/api1`, `/api2`, `/api3`.

You can call these APIs using the CURL commands:

```
curl http://<cluster-public-ip>:32600/api1
curl http://<cluster-public-ip>:32600/api2
curl http://<cluster-public-ip>:32600/api3
```

The API invocations update a file, `apistats.csv` in the container's volume mount path `/mydata`. This file keeps count of the number of times respective APIs are called. Go ahead and call these APIs multiple times.

You should verify if the file `apistats.csv` is updated whenever the APIs are called.

Get into the container shell using the command:

```
kubectl exec -it <pod_name> -n mlp-ns -- /bin/sh
```

Now, change the directory to `/mydata`. You should find a file named `apistats.csv`. Print the contents of the file to see the logged data.

```
cd /mydata
cat apistats.csv
```

The output should look similar to this:

```
api,count
api1,1
api2,3
api3,1
```

Congrats, you have simulated the existing setup.

### 3. Prepare the code for migration

This section helps you to understand about the changes required for migration. Make a note that the tutorial provides you the modified code which is located at `migrate-apps-from-k8s-to-ocp/deploy-to-openshift` so you do not need to make any changes. The following details are listed for your reference.

#### 3.1 Image migration

Please refer to the following when modifying the Dockerfile:

* [Migrate your Kubernetes images to OpenShift](https://developer.ibm.com/learningpaths/migrate-kubernetes-openshift/migrate-images/)
* [Best practices for designing a Universal Application Image](https://developer.ibm.com/learningpaths/universal-application-image/design-universal-image/)

The modified Dockerfile is provided in the cloned repo at `~/migrate-apps-from-k8s-to-ocp/deploy-to-openshift`. Here are the contents of that file:

```
FROM registry.access.redhat.com/ubi8/nodejs-14:1-28 AS builder

WORKDIR /app
COPY app/ /app

# Install dependencies
RUN npm install

# Build our deployable image based on UBI
FROM registry.access.redhat.com/ubi8/nodejs-14:1-28

USER root

## Update security
RUN dnf -y update-minimal --security --sec-severity=Important --sec-severity=Critical && \
    dnf clean all

USER 1001
WORKDIR /app
COPY --from=builder /app .

ENV WEB_PORT 3000
EXPOSE  3000

# Define command to run the application when the container starts
CMD ["node", "/app/app.js"]
```

In this example, note the follwing best practices that were used to bulid the image. The image:

* Used a Red Hat UBI as its base image
* Included the latest security updates
* Used a two-stage image build
* Defined the user ID to avoid any root user process

> Note: If you want to build an image that can pass Red Hat certification, you may need to add a label, license fil, and other information in your Dockerfile. You can read more in this article: [Best practices for designing a universal application image](https://developer.ibm.com/learningpaths/universal-application-image/design-universal-image/).

You can also use the [Cloud-native toolkit](https://cloudnativetoolkit.dev) to build your OpenShift certifiable image. Read the learning path [Build Images with the Cloud-Native Toolkit](https://developer.ibm.com/learningpaths/build-images-cloud-native-toolkit/) for more information.

#### 3.2 Kubernetes PSP to OpenShift SCC migration

The article [Migrate your Kubernetes pod security policies to OpenShift security context constraints](https://developer.ibm.com/learningpaths/migrate-kubernetes-openshift/migrate-kubernetes-psp-openshift-scc/) explains exactly what you need to do to migrate your PSPs to SCCs.

When `psp.yaml` is migrated to `scc.yaml`, it should look as below:

```
kind: SecurityContextConstraints
apiVersion: v1
metadata:
  name: mlp-scc
allowPrivilegedContainer: false
runAsUser:
  type: MustRunAsRange
  uidRangeMin: 1000
  uidRangeMax: 2000
seLinuxContext:
  type: RunAsAny
fsGroup:
  type: MustRunAs
  ranges:
  - min: 5000
    max: 6000
supplementalGroups:
  type: MustRunAs
  ranges:
  - min: 5000
    max: 6000
  volumes:
  - 'secret'
  - 'emptyDir'    
```

Note that some fields are different in `scc.yaml` than in `psp.yaml`.

* Kind changed from `PodSecurityPolicy` to `SecurityContextConstraints`
* `privileged` changed to `allowPrivilegedContainer`
* The way user and group ranges are specified is different
* No changes in the way volumes are controlled

Similarly, the `rbac.yaml` is also migrated and located in `deploy-to-openshift` folder in the Git repo.

### 4. Deploy the migrated application on OpenShift

**4.1 Build your container image**

As mentioned in Step 2, you need to build the container image of your application.

> Note: This tutorial uses DockerHub as image registry. You may choose an integrated image registry or any other image registry of your choice.

```
cd migrate-apps-from-k8s-to-ocp/deploy-to-openshift/
cp -pr ../app .
docker build -t <your-docker-account>/ocp-image .
docker push <your-docker-account>/ocp-image
```
Make a note of your image URL `<your-docker-account>/ocp-image`. Modify `deploy.yaml` using the following command.

```
sed -i '' s#IMAGE#<your-docker-account>/ocp-image# deploy.yaml
```

**4.2 Deploy the application**

Log in to your OpenShift cluster using a terminal window.

From the IBM Cloud console go to `Clusters > Your OpenShift Cluster > OpenShift web console`. On the OpenShift web console click the menu in the upper right corner (the label contains your email address), and select `Copy Login Command`. Click on Display token and paste the command into a terminal session to login to your OpenShift cluster.

```
oc login --token=xxxx --server=https://xxxx.containers.cloud.ibm.com:xxx
```

This tutorial uses the same name for the namespace `mlp-ns` and the service account `mlp-sa` as in Kubernetes.

Execute the commands below.

```
oc new-project mlp-ns
oc project mlp-ns
oc create serviceaccount mlp-sa
```

From a terminal window, navigate to the `deploy-to-openshift` folder of your cloned repository.

Execute the following commands.

```
cd migrate-apps-from-k8s-to-ocp/deploy-to-openshift

## Deploy pod security policy using the file `scc.yaml`
oc apply -f scc.yaml

## Deploy rbac using the file `rbac.yaml`
oc apply -f rbac.yaml

## Deploy the application using the deployment file `deploy.yaml`
oc apply -f deploy.yaml

## Verify that the application is deployed fine.
oc get pods
```

Verify what SCC is applied to the pod by running the following command:

```
oc get pod <pod_name> -o yaml | grep scc
```

The output should look similar to this:

```
openshift.io/scc: mlp-scc
```

Notice that `mlp-scc` SCC is applied for the pod deployment.

Expose the service and get the route to access the application.

```
oc expose svc mlp-service
oc get routes | grep mlp
```

You can access the deployed application using this route.

### 5. Analyze the results

You can access the application using `http://<route>`. You can invoke the APIs using the CURL commands:

```
curl http://<route>/api1
curl http://<route>/api2
curl http://<route>/api3
```

Go ahead and call these APIs multiple times.

To check the `apistats.csv` file, access the container using the command:

```
oc rsh <pod_name>
```

Now change the directory to `/mydata`. Print the contents of the file `apistats.csv` to see the logged data.

```
cd /mydata
cat apistats.csv   ## You should see output something like this, similiar to Kubernetes

api,count
api1,2
api2,5
api3,1
```

Congrats! You successfully migrated the application from Kubernetes to OpenShift by modifying the images and pod permissions.

> Note that, for the purpose of this tutorial, a mount path was used within the container instead of persistent volume. Because of this, the content of `apistats.csv` file is not migrated along with application. This file will be newly created for each container deployed.

### Troubleshooting

Below are a few possible issues that you could encounter as well as their resolutions. This is not an exhaustive list, but just some common problems and their resolutions.

#### Application does not get deployed on OpenShift

Check the events using the command `oc get events`.

**Case 1**: The events shows `unable to validate against any security context constraint: Invalid value: xxxx: must be in the ranges: [yyyy, zzzzz]]`

Possible causes for this error are:
- The correct SCC is not applied for the deployment. Ensure Role and Rolebinding are in place so that the correct SCC can be applied.
- The SCC does not allow the users specified in the deployment file. Ensure your SCC permits the users specified in deployment to deploy the pods.

**Case 2**: The events shows `unable to validate against any security context constraint: [spec.volumes[0]: Invalid value: "emptyDir": emptyDir volumes are not allowed to be used provider restricted`

This error is caused if your SCC does not allow `emptyDir` volumes to be used. Ensure that `emptyDir` is permitted under `volumes` in `scc.yaml` file.

Similarly, check for errors for other parameters and resolve the issues.

#### Application has additional container permissions than defined in the SCC

In Kubernetes, the control key to specify the policy to allow privileged containers is `privileged`. The same control key in OpenShift is `allowProvilegedContainer`. Also `allowProvilegedContainer` is `true` by default. Therefore, it is important to ensure that this flag is set with right value.

To verify the value of the flag, run the command `oc get scc mlp-scc -o yaml`. In the output, verify the correct values are set for `allowPrivilegeEscalation`. Similarly, verify all corresponding flags from PSP are available and set with the right values.

### Summary

This tutorial demonstrated the process of application migration from Kubernetes to OpenShift using a sample application. It highlights migration aspects in two areas:
- Image migration: followed best practices for container images
- Pod security consideration: migrate pod security permissions to security context constraints