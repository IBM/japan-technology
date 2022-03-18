---
also_found_in:
- learningpaths/dataops-fundamentals/
authors: ''
completed_date: '2021-10-19'
components:
- cloud-pak-for-data
draft: false
excerpt: Virtualize enterprise data using business terms using Data Virtualization
  on IBM Cloud Pak for Data.
meta_description: Virtualize enterprise data using business terms using Data Virtualization
  on IBM Cloud Pak for Data.
meta_keywords: IBM Cloud Pak for Data, Data Virtualization, data, databases
meta_title: Create a single customer view of your data with data virtualization
primary_tag: analytics
subtitle: Virtualize your data using business terms to ensure that the data is governed
  and protected
tags:
- data-management
title: Create a single customer view of your data with data virtualization
---

Enterprise data is often spread across various data stores, such as data marts, data warehouses, and data lakes. Companies often seek to break down these silos by copying all of the data into a central store for analysis. Such duplication of data can cause issues such as stale data and additional costs for managing the central data store.

*Data virtualization* is a data management approach that provides the ability to query multiple data sources without copying and replicating the data, thereby reducing costs. It can be used to generate a single customer view of the data irrespective of where the data is located and how the data is formatted. 

In this tutorial, learn how to virtualize governed and protected enterprise data using Data Virtualization on IBM Cloud Pak for Data, and join the virtual data to create a single customer view of the data.

## Learning objectives

In this tutorial, you:

* Add a data source for data virtualization
* Virtualize the data with business terms
* Create a joined virtual view
* Assign governance terms and data classes to the columns in the virtual view
* Provide users with permission to access the virtual view
* Log in as various users to access the virtual view and add it to an analytics project

## Prerequisites

* [IBM Cloud Pak for Data v4.0](https://www.ibm.com/products/cloud-pak-for-data)
* [Watson Knowledge Catalog on IBM Cloud Pak for Data](https://www.ibm.com/docs/en/cloud-paks/cp-data/latest?topic=services-watson-knowledge-catalog)
* [Data Virtualization on IBM Cloud Pak for Data](https://www.ibm.com/docs/en/cloud-paks/cp-data/latest?topic=services-data-virtualization)
* The steps in [Protect your data using data privacy features](https://developer.ibm.com/tutorials/protect-your-data-using-data-privacy-features) must be completed.

## Estimated time

It should take you approximately 45-60 minutes to complete the tutorial.

## Step 1. Provision Data Virtualization on IBM Cloud Pak for Data

Start by provisioning Data Virtualization on your IBM Cloud Pak for Data instance.

### Log in to IBM Cloud Pak for Data

1. Log in to your IBM Cloud Pak for Data instance as the **admin** user.
  
    ![CPD login](images/cpd-login.png)

### Provision Data Virtualization on IBM Cloud Pak for Data

1. Go to  the **hamburger (☰)** menu, expand **Services**, and click **Services catalog**.

    ![Go to services catalog](images/cpd-services-catalog.png)

1. Choose the **Data sources** category on the left, and then click the tile for **Data Virtualization**.
   
    ![Services - DV](images/cpd-service-dv.png)

1. Click **Provision instance**.
   
    ![Deploy data virtualization](images/cpd-deploy-data-virtualization.png)

1. Follow the instructions to provision the Data Virtualization instance.

**Note**: For deployment using Managed OpenShift, you must do the following:

1. Decide whether to check the **Updated the kernel semaphore parameter** checkbox.
1. Do *NOT* choose the defaults for storage. If you use Portworx storage, select **portworx-db2-rwx-sc** as the storage class. Otherwise, choose **ibmc-file-gold-gid** as the storage class.

## Step 2. Add a new data source connection to Data Virtualization

You already added your IBM Db2 on Cloud service instance as a Platform connection to IBM Cloud Pak for Data as part of the [Learn to discover data that resides in your data sources](/tutorials/learn-to-discover-data-that-resides-in-your-data-sources) tutorial. You now add the same data source as a connection in Data Virtualization.

**Note**: If your data source is in a remote data center (not in the same data center as the IBM Cloud Pak for Data instance), you can improve the performance of your data source connections using remote connectors. Follow the instructions in the [Improve performance for your data virtualization data sources with remote connectors](/tutorials/improve-performance-for-your-database-connections-with-remote-connectors/) tutorial to set up a remote connector for your data source.

1. Go to the **hamburger (☰)** menu, expand **Data**, and click **Data virtualization**.
  
    ![Hamburger menu - Data Virtualization](images/cpd-menu-data-virtualization.png)

1. Open the Data Virtualization menu. Expand **Virtualization** within the menu, and click **Data sources**.
   
    ![DV - Go to data sources](images/dv-data-sources.png)

1. Click **Add connection +**, then click **Existing connection**.
   
    ![DV - select existing data source](images/dv-select-existing-data-source.png)

1. Select your Db2 connection from the list of connections, and click **Add**.
   
    ![DV - add data source](images/dv-add-data-source.png)
    
    **Note**: Remember to select the same Db2 connection that was used for discovering the data in the [Learn to discover data that resides in your data sources](/tutorials/learn-to-discover-data-that-resides-in-your-data-sources) tutorial.
    
1. Click **Skip**.
   
    ![DV - skip remote connectors](images/dv-datasource-skip-rc.png)

1. The data connection is added as a data source for Data Virtualization, and you should see the data connection listed on the **Data sources** screen.
   
    ![DV - data source added](images/dv-data-source-added.png)

## Step 3. Create virtual tables and views using data virtualization

Now that the data source is available in Data Virtualization, you can virtualize the data tables within the data source. After the tables are virtualized, you can create virtual views by joining the virtual tables.

### Virtualize the tables with business terms

1. Open the Data virtualization menu, expand **Virtualization**, and click **Virtualize**.
   
    ![DV - menu - virtualize](images/dv-menu-virtualize.png)

1. Several tables appear. Find and select the **PATIENTS** and **ENCOUNTERS** table contained in the Db2 connection that you added. You can also search for the tables using the search bar. When selected, click **Add to cart**, then **View cart**.
   
    ![DV - add to cart](images/dv-add-to-cart.png)
    
    **Note**: In addition to the **PATIENTS** and **ENCOUNTERS** tables, you can also select the other tables from the Healthcare data set, provided that you uploaded them to your Db2 database.

1. The next screen prompts you to choose whether you want to assign the virtualized data to a *data request*, a *project*, or to your *virtualized data*. Choose **My virtualized data**. Click the three vertical dots for the **PATIENTS** table to open the overflow menu, and click **Edit columns**.
   
    ![DV - view cart](images/dv-view-cart.png)

1. Click the checkbox for **Replace all columns with business terms**. This replaces the names of all of the columns in the table with the [business terms that were assigned to these columns](/tutorials/analyze-discovered-data-to-gain-insights-on-the-quality-of-your-data#step-1-review-and-update-data-classes-business-terms-and-keys-for-the-data-assets). Click **Apply** to apply the changes.
   
    ![DV - patients - business terms](images/dv-patients-business-terms.png)

1. Repeat the steps to replace the column names with business terms for the **ENCOUNTERS** table, then click **Virtualize**.
   
    ![DV - virtualize](images/dv-virtualize.png)
    
    **Note**: If you have added other tables to your cart in addition to **PATIENTS** and **ENCOUNTERS**, you can also replace the column names with the business terms for all of those tables as long as you had previously assigned business terms for the tables and published the tables to the Default catalog.

1. You see a notification that the virtual tables have been created. To see the newly virtualized data, click **View my virtualized data**.
   
    ![DV - virtualize completed](images/dv-virtualize-completed.png)

### Create a merged view by joining the virtualized data

The next step is to join the virtual tables that have been created to create a merged view of the data. One option to get a merged set of data from multiple tables is to use a notebook to write multiple lines of code that join the data. Data virtualization, on the other hand, makes it much easier to handle joins between multiple data assets. Joining data assets using data virtualization only requires a few mouse clicks.

1. Select the **PATIENTS** and **ENCOUNTERS** tables, and click the **Join** button.
   
    ![DV - view virtualized data](images/dv-view-virtualized-data.png)

1. The columns of both the tables are shown on the screen. You can see that the business terms for the columns are displayed as the column names because you chose to replace the column names with business terms when you virtualized the tables.

1. To join the tables, you must pick a key that is common to both tables. In this case, the **Patient ID** column is common between the two tables, and you can mark this column as the key by clicking the **Patient ID** column in one table and dragging it to the **Patient ID** column in the other table. When you see a line or curve connecting the columns in the two tables, click **Next**.
   
    ![DV - select join key](images/dv-select-join-key.png)

1. You can edit the column names for the joined view. Because the original column names already have been replaced with the business terms, you can leave the column names as they are. Click **Next**.
   
    ![DV - joined column names](images/dv-joined-column-names.png)

1. On the next screen, provide a name for the joined view (`PATIENTS_ENCOUNTERS`). Under **Assign to**, choose **My virtualized data**. Click **Create view**.
   
    ![DV - create joined view](images/dv-create-joined-view.png)

1. You are notified that the join has succeeded. Click **View my virtualized data** to view your virtualized data.
   
    ![DV - view virtualized data 2](images/dv-view-virtualized-data-2.png)

## Step 4. Grant users with access to published view

Now that the virtual view has been created and published to the Default Catalog, you can provide users with access to the published view. To do this, the users must be granted access to the Default Catalog as well as Data Virtualization.

**Note**: You are granting access to the published view to the two users **regular_user** and **restricted_user** that were used to [verify the enforcement of the data protection rules](/tutorials/protect-your-data-using-data-privacy-features/#step-7-verify-the-data-protection-rules-are-enforced). These users were already granted access to the Default catalog and only need to be granted access rights to Data Virtualization now.

### Grant Data Virtualization access to users

IBM Cloud Pak for Data users that need to use data virtualization functions must be assigned specific roles based on their job descriptions. These roles are Admin, Engineer, User, and Steward. You can learn more about these roles in the [IBM Cloud Pak for Data documentation](https://www.ibm.com/docs/en/cloud-paks/cp-data/latest?topic=virtualization-managing-roles-users-groups).

1. Click **My virtualized data** to open the Data Virtualization menu, then click **User management**.
   
    ![DV - user management](images/dv-user-management.png)

1. Click **Grant access +**. In the pop-up window, select the users that you want to add to Data Virtualization. Using the drop-down menu, provide the **User** role to each of these users. Click **Add**.
   
    ![DV - add users to DV](images/dv-add-users-to-dv.png)

## Step 5. Update business terms and data classes for the published virtual view

Earlier, you were able to [virtualize the tables using business terms](#virtualize-the-tables-with-business-terms). These business terms came from the tables that were discovered and subsequently published to the Default Catalog. However, the virtual tables only had the column names replaced with the business terms. The virtual tables do not have any data class and business term assignments that were made during [analysis of the discovered tables](/tutorials/analyze-discovered-data-to-gain-insights-on-the-quality-of-your-data).

You now update the published virtual view with the correct data classes and business terms.

**Note**: Updating the data classes and business terms here is important for the [previously created data protection rules](/tutorials/protect-your-data-using-data-privacy-features) to be applied to the virtual view. In the absence of the correct data classes and business terms, the data is not protected (by denial of access, masking, substituting, or obfuscating), and the users are able to see all of the original data.

1. Go to the **hamburger (☰)** menu, expand **Catalogs**, and click **All catalogs**.
   
    ![CPD - menu - all catalogs](images/cpd-menu-all-catalogs.png)

1. Click the tile for the **Default Catalog**.
   
    ![CPD - default catalog](images/cpd-default-catalog.png)

1. Scroll down, and click the name of the **ADMIN.PATIENTS_ENCOUNTERS** asset.
   
    ![Catalog - PE asset](images/catalog-pe-asset.png)

### Create a data profile for the published view

1. Go to the **Profile** tab. Click **Create profile**. Watson Knowledge Catalog now looks at the first 5,000 rows from the view to identify and assign data classes for all of the columns. 
   
    ![Catalog - PE asset - profile](images/catalog-pe-asset-profile.png)

1. Creating the data profile can take some time. You might need to refresh the page occasionally to check the status.
   
    ![Catalog - PE asset - refresh profile](images/catalog-pe-asset-refresh-profile.png)

### Update data classes for the published view

1. Watson Knowledge Catalog attempts to identify data classes for all of the columns and selects one data class for each column. You can go through the data classes that have been identified and assigned for each column and correct the ones that are incorrectly assigned. For example, the Encounter Code column has been assigned the `Numeric` data class. To update the data class, click the arrow under the column name Encounter Code. A list of other data classes that have been suggested by Watson Knowledge Catalog is displayed. You can select a new data class by clicking one of the data classes listed here or by clicking **View all** to pick a data class that was not suggested by Watson Knowledge Catalog. For the Encounter Code column, click the correct data class, **Encounter code**.
   
    ![Catalog - PE asset - update data class](images/catalog-pe-asset-update-data-class.png)

1. The data class for Encounter Code column is updated. Repeat the process to verify and update the data classes for all of the other columns in the asset. You can refer to the [Data Asset Annotations file](https://s3.us-east.cloud-object-storage.appdomain.cloud/staging-sombra/default/tutorials/analyze-discovered-data-to-gain-insights-on-the-quality-of-your-data/static/data-asset-annotations.pdf) to obtain the data classes for the columns in this asset. Remember to use the data classes assigned to the columns in the **PATIENTS** and **ENCOUNTERS** tables because the PATIENTS_ENCOUNTERS view was created by joining these two tables.

### Update business terms for the published view

1. Go to the **Asset** tab. You can see the updated data classes under each column. You can now update the business terms for the columns. For the first column Encounter ID, click the eye icon next to the column name.
   
    ![Catalog - PE asset - asset tab](images/catalog-pe-asset-asset-tab.png)

1. In the pop-up window, click the pencil icon next to Business terms.
   
    ![Catalog - PE asset - update business terms 1](images/catalog-pe-asset-update-business-terms-1.png)

1. Search for and select the Encounter ID business term. Click **Apply**, then **Close**. The business term for the Encounter ID column are updated.
   
    ![Catalog - PE asset - update business terms 2](images/catalog-pe-asset-update-business-terms-2.png)

1. Repeat the process to update the business terms for all of the other columns in the asset. You can refer to the [Data Asset Annotations file](https://s3.us-east.cloud-object-storage.appdomain.cloud/staging-sombra/default/tutorials/analyze-discovered-data-to-gain-insights-on-the-quality-of-your-data/static/data-asset-annotations.pdf) to obtain the business terms for the columns in this asset. Remember to use the business terms assigned to the columns in the **PATIENTS** and **ENCOUNTERS** tables because the PATIENTS_ENCOUNTERS view was created by joining these two tables.

## Step 6. Users view and assign the virtualized data to a project

Next, you can log in as the users to verify what data they can see and how they can add the virtualized data to their projects.

### Log into IBM Cloud Pak for Data as a non-admin user

1. Log out of IBM Cloud Pak for Data, and log back in as **regular_user**.
   
    ![CPD login](images/cpd-login.png)

### Create analytics project

1. Go to the **hamburger (☰)** menu, expand **Projects**, and click **All projects**.
   
    ![Go to projects](images/cpd-go-to-projects.png)

1. Click **New project +**. In the pop-up window, select **Analytics project**, then click **Next**.
   
    ![Start a new project](images/cpd-new-project.png)

1. Click the tile for **Create an empty project**.
   
    ![Create empty project](images/cpd-create-empty-project.png)

1. Provide a name (`Healthcare Project`) and an optional description (`Healthcare project created by regular user`) for the project, and click **Create**.
   
    ![Create project](images/cpd-create-project.png)

### Assign the published data to a project

1. Go to the **hamburger (☰)** menu, expand **Catalogs**, and click **All catalogs**.
   
    ![CPD - all catalogs](images/cpd-all-catalogs.png)

1. Click the tile for the **Default Catalog**.
   
    ![CPD - go to default catalog](images/cpd-go-to-default-catalog.png)

1. Scroll down, and click the name of the **ADMIN.PATIENTS_ENCOUNTERS** asset.
   
    ![Catalog - PE asset](images/catalog-pe-asset.png) 

1. Go to the **Asset** tab. You might be asked to enter your credentials to unlock the Data Virtualization asset. Provide your username (`regular_user`) and password, and click **Connect**.
   
    ![Catalog - provide DV credentials](images/catalog-provide-dv-credentials.png)

1. It might take a while for the data masking process to complete, and you might have to refresh the page. After the asset loads, you are able to see the data classes that have been assigned for each column. For example, the first column Encounter ID has the data class `UUID`. Click the eye icon next to the column name Encounter ID. A new window opens, and you can see that the Encounter ID business term has been assigned to this column. Click **Close** to close the window.
   
    ![Catalog - assigned business term](images/catalog-assigned-business-term.png)

1. Notice that five colums in the view are masked. Clicking on the lock icon tells you how many columns were masked using the different masking techniques.
   
    ![Catalog - masked columns](images/catalog-masked-columns.png)

1. The columns that are masked are Patient Birth Date, Patient SSN, Patient Race, Patient Ethnicity, and Patient Gender. All masked columns have a lock icon next to the column name. Clicking the lock icon gives you more information on why the column was masked.
   
    ![Catalog - masked column details](images/catalog-masked-column-details.png)

1. The columns are being masked due to the data protection rules that were [previously](h/tutorials/protect-your-data-using-data-privacy-features) set up.

1. To add this data to your analytics project, click **Add to project +**.
   
    ![Catalog - add to project](images/catalog-add-to-project.png)

1. Under Target, select your project **Healthcare Project**, and click **Add**.
   
    ![Catalog - select target](images/catalog-select-target.png)

1. You see a notification that two assets were successfully added to the project. Click **Go to project**.
   
    ![Catalog - go to project](images/catalog-go-to-project.png)

1. Go to the **Assets** tab. You see two entries: one for the Data Virtualization connection and another for the ADMIN.PATIENTS_ENCOUNTERS asset. Click the **ADMIN.PATIENTS_ENCOUNTERS** asset.
   
    ![Project - go to asset](images/project-go-to-asset.png)

1. Use your user name `regular_user` and its password if you are asked to enter the credentials to unlock the Data Virtualization connection, and click **Connect**.
   
    ![Project - provide credentials](images/project-provide-credentials.png)

1. On the **Preview** tab of the asset, you are able to preview the data. You see that the data masking that was performed in the catalog is propagated to the asset in the project, and the asset is protected in the same manner if any other operations such as Data Refinement are performed on it.

    ![Project - view protected asset](images/project-view-protected-asset.png)

1. Log out of IBM Cloud Pak for Data, and log back in as the **restricted_user**. If you attempt to perform the previous steps to go to the Default Catalog and access the published virtual view ADMIN.PATIENTS_ENCOUNTERS, you see an error. This is due to another data protection rule that prevents the restricted_user from accessing any data asset that has a column with the data class Passport or a column with the business term Patient Driver's License.
   
    ![Catalog - restricted_user](images/catalog-restricted-user.png)

## Summary

In this tutorial, you learned to use Data Virtualization on IBM Cloud Pak for Data to virtualize data that has been protected using data protection rules within Watson Knowledge Catalog on IBM Cloud Pak for Data. You saw how column names of the virtualized data can be replaced with the previously assigned business terms, thereby ensuring that the data column names are standardized as per the enterprise policies. You learned how to join virtualized data to create a virtual view and how to update the data classes and business terms for the newly created virtual view. This ensured that the data protection rules that were defined earlier are enforced. You verified that the data protection rules are enforced by logging in as other non-admin users to access and assign the virtual view to a project. This ensured that while the real data is not visible to users, they can use the columns that exist and based on the type of data masking used, they can also get an idea about the formats or table references of those columns.

This tutorial is part of the [An introduction to the DataOps discipline](https://developer.ibm.com/articles/an-introduction-to-the-dataops-discipline) series.