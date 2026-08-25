// Jenkins Pipeline for Bob AI Integration
//
// This Jenkinsfile demonstrates how to integrate Bob into your Jenkins CI/CD
// pipeline for automated code review, security scanning, and quality checks.
//
// Copy this content to a file named 'Jenkinsfile' in your repository root

pipeline {
    agent any
    
    // Environment variables
    environment {
        BOB_API_KEY = credentials('bob-api-key')  // Jenkins credential ID
        BOB_VERSION = 'latest'
        QUALITY_THRESHOLD = '70'
        REPORTS_DIR = 'bob-reports'
    }
    
    // Build parameters
    parameters {
        choice(
            name: 'ANALYSIS_LEVEL',
            choices: ['standard', 'thorough', 'quick'],
            description: 'Level of analysis to perform'
        )
        booleanParam(
            name: 'FAIL_ON_SECURITY',
            defaultValue: true,
            description: 'Fail build on critical security issues'
        )
        booleanParam(
            name: 'GENERATE_DOCS',
            defaultValue: false,
            description: 'Generate documentation'
        )
    }
    
    // Pipeline options
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
        disableConcurrentBuilds()
    }
    
    // Stages
    stages {
        
        // Stage 1: Setup
        stage('Setup') {
            steps {
                script {
                    echo "Setting up Bob CLI..."
                    
                    // Install Bob CLI
                    sh '''
                        npm install -g @ibm/bob-cli@${BOB_VERSION}
                        bob --version
                    '''
                    
                    // Configure Bob
                    sh '''
                        bob config set api-key ${BOB_API_KEY}
                        bob config set cache-enabled true
                        bob config set cache-dir .bob-cache
                    '''
                    
                    // Create reports directory
                    sh "mkdir -p ${REPORTS_DIR}"
                    
                    echo "Setup completed successfully"
                }
            }
        }
        
        // Stage 2: Code Review
        stage('Code Review') {
            when {
                anyOf {
                    changeRequest()
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                script {
                    echo "Running code review..."
                    
                    def targetBranch = env.CHANGE_TARGET ?: 'main'
                    
                    sh """
                        bob "Review the code changes between origin/${targetBranch} and HEAD. Focus on code quality, potential bugs, and best practices. Output the review in markdown format." > ${REPORTS_DIR}/review-report.md || true
                    """
                    
                    // Check if review was successful
                    if (fileExists("${REPORTS_DIR}/review-report.md")) {
                        echo "Code review completed successfully"
                        
                        // Read and display summary
                        def reviewContent = readFile("${REPORTS_DIR}/review-report.md")
                        echo "Review Summary:\n${reviewContent.take(500)}..."
                    } else {
                        echo "Warning: Review report not generated"
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: "${REPORTS_DIR}/review-report.md", allowEmptyArchive: true
                }
            }
        }
        
        // Stage 3: Security Scan
        stage('Security Scan') {
            steps {
                script {
                    echo "Running security scan..."
                    
                    sh """
                        bob "Perform a comprehensive security scan of the codebase. Focus on high and critical severity vulnerabilities. Output results in JSON format." > ${REPORTS_DIR}/security-report.json || true
                    """
                    
                    // Parse security results
                    if (fileExists("${REPORTS_DIR}/security-report.json")) {
                        def securityReport = readJSON file: "${REPORTS_DIR}/security-report.json"
                        
                        def criticalCount = securityReport.critical?.size() ?: 0
                        def highCount = securityReport.high?.size() ?: 0
                        def mediumCount = securityReport.medium?.size() ?: 0
                        
                        echo "Security Issues Found:"
                        echo "  Critical: ${criticalCount}"
                        echo "  High: ${highCount}"
                        echo "  Medium: ${mediumCount}"
                        
                        // Set build status
                        if (criticalCount > 0) {
                            if (params.FAIL_ON_SECURITY) {
                                error("Critical security issues found: ${criticalCount}")
                            } else {
                                unstable("Critical security issues found: ${criticalCount}")
                            }
                        } else if (highCount > 0) {
                            unstable("High severity security issues found: ${highCount}")
                        }
                    } else {
                        echo "Warning: Security report not generated"
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: "${REPORTS_DIR}/security-report.json", allowEmptyArchive: true
                }
            }
        }
        
        // Stage 4: Quality Analysis
        stage('Quality Analysis') {
            steps {
                script {
                    echo "Running quality analysis..."
                    
                    sh """
                        bob "Analyze the codebase for quality, performance, and maintainability issues. Provide an overall quality score and detailed metrics in JSON format." > ${REPORTS_DIR}/quality-report.json || true
                    """
                    
                    // Parse quality results
                    if (fileExists("${REPORTS_DIR}/quality-report.json")) {
                        def qualityReport = readJSON file: "${REPORTS_DIR}/quality-report.json"
                        
                        def score = qualityReport.overall_score ?: 0
                        echo "Overall Quality Score: ${score}/100"
                        
                        // Check against threshold
                        if (score < QUALITY_THRESHOLD.toInteger()) {
                            unstable("Quality score ${score} is below threshold ${QUALITY_THRESHOLD}")
                        } else {
                            echo "Quality check passed!"
                        }
                        
                        // Display metrics
                        if (qualityReport.metrics) {
                            echo "Quality Metrics:"
                            qualityReport.metrics.each { key, value ->
                                echo "  ${key}: ${value}"
                            }
                        }
                    } else {
                        echo "Warning: Quality report not generated"
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: "${REPORTS_DIR}/quality-report.json", allowEmptyArchive: true
                }
            }
        }
        
        // Stage 5: Complexity Analysis
        stage('Complexity Analysis') {
            when {
                expression { params.ANALYSIS_LEVEL == 'thorough' }
            }
            steps {
                script {
                    echo "Running complexity analysis..."
                    
                    sh """
                        bob "Analyze the codebase for complexity metrics including cyclomatic complexity and cognitive complexity. Output results in JSON format." > ${REPORTS_DIR}/complexity-report.json || true
                    """
                    
                    if (fileExists("${REPORTS_DIR}/complexity-report.json")) {
                        def complexityReport = readJSON file: "${REPORTS_DIR}/complexity-report.json"
                        
                        // Find high complexity functions
                        def highComplexity = complexityReport.functions?.findAll { it.complexity > 10 }
                        
                        if (highComplexity) {
                            echo "High Complexity Functions Found: ${highComplexity.size()}"
                            highComplexity.take(5).each { func ->
                                echo "  ${func.name}: Complexity ${func.complexity}"
                            }
                        } else {
                            echo "No high complexity functions found"
                        }
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: "${REPORTS_DIR}/complexity-report.json", allowEmptyArchive: true
                }
            }
        }
        
        // Stage 6: Dependency Check
        stage('Dependency Check') {
            when {
                expression { fileExists('package.json') || fileExists('requirements.txt') }
            }
            steps {
                script {
                    echo "Checking dependencies..."
                    
                    if (fileExists('package.json')) {
                        sh """
                            bob "Analyze package.json for dependency issues and vulnerabilities. Check for outdated packages and security issues. Output results in JSON format." > ${REPORTS_DIR}/dependency-report.json || true
                        """
                        
                        if (fileExists("${REPORTS_DIR}/dependency-report.json")) {
                            def depReport = readJSON file: "${REPORTS_DIR}/dependency-report.json"
                            
                            def vulnerableCount = depReport.vulnerable?.size() ?: 0
                            def outdatedCount = depReport.outdated?.size() ?: 0
                            
                            echo "Vulnerable Dependencies: ${vulnerableCount}"
                            echo "Outdated Dependencies: ${outdatedCount}"
                            
                            if (vulnerableCount > 0) {
                                unstable("Vulnerable dependencies found: ${vulnerableCount}")
                            }
                        }
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: "${REPORTS_DIR}/dependency-report.json", allowEmptyArchive: true
                }
            }
        }
        
        // Stage 7: Generate Documentation
        stage('Generate Documentation') {
            when {
                anyOf {
                    branch 'main'
                    expression { params.GENERATE_DOCS }
                }
            }
            steps {
                script {
                    echo "Generating documentation..."
                    
                    sh """
                        mkdir -p docs
                        
                        bob "Generate comprehensive API documentation in HTML format from the codebase" > docs/api.html || true
                        
                        bob "Generate architecture documentation in HTML format showing the system design and component relationships" > docs/architecture.html || true
                        
                        bob "Create a comprehensive README from the codebase" > docs/README.md || true
                    """
                    
                    echo "Documentation generated successfully"
                }
            }
            post {
                success {
                    publishHTML([
                        reportDir: 'docs',
                        reportFiles: 'api.html',
                        reportName: 'API Documentation',
                        keepAll: true
                    ])
                    archiveArtifacts artifacts: 'docs/**/*', allowEmptyArchive: true
                }
            }
        }
        
        // Stage 8: Generate Summary
        stage('Generate Summary') {
            steps {
                script {
                    echo "Generating summary report..."
                    
                    def summary = """
# Bob AI Analysis Summary

**Build:** ${env.BUILD_NUMBER}
**Branch:** ${env.BRANCH_NAME}
**Commit:** ${env.GIT_COMMIT?.take(8)}
**Date:** ${new Date()}

## Results

"""
                    
                    // Add code review results
                    if (fileExists("${REPORTS_DIR}/review-report.md")) {
                        summary += "### ✅ Code Review\nReview completed successfully\n\n"
                    } else {
                        summary += "### ❌ Code Review\nReview failed or not run\n\n"
                    }
                    
                    // Add security scan results
                    if (fileExists("${REPORTS_DIR}/security-report.json")) {
                        def securityReport = readJSON file: "${REPORTS_DIR}/security-report.json"
                        def criticalCount = securityReport.critical?.size() ?: 0
                        def highCount = securityReport.high?.size() ?: 0
                        
                        if (criticalCount == 0) {
                            summary += "### ✅ Security Scan\n"
                        } else {
                            summary += "### ❌ Security Scan\n"
                        }
                        summary += "- Critical Issues: ${criticalCount}\n"
                        summary += "- High Issues: ${highCount}\n\n"
                    }
                    
                    // Add quality analysis results
                    if (fileExists("${REPORTS_DIR}/quality-report.json")) {
                        def qualityReport = readJSON file: "${REPORTS_DIR}/quality-report.json"
                        def score = qualityReport.overall_score ?: 0
                        summary += "### 📊 Quality Analysis\n"
                        summary += "Overall Score: ${score}/100\n\n"
                    }
                    
                    summary += """
## Artifacts

- [Code Review Report](${REPORTS_DIR}/review-report.md)
- [Security Report](${REPORTS_DIR}/security-report.json)
- [Quality Report](${REPORTS_DIR}/quality-report.json)

---
*Generated by Bob AI*
"""
                    
                    writeFile file: "${REPORTS_DIR}/summary.md", text: summary
                    echo summary
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: "${REPORTS_DIR}/summary.md", allowEmptyArchive: true
                }
            }
        }
    }
    
    // Post-build actions
    post {
        always {
            // Clean up workspace
            cleanWs(
                deleteDirs: true,
                patterns: [
                    [pattern: '.bob-cache', type: 'INCLUDE'],
                    [pattern: 'node_modules', type: 'INCLUDE']
                ]
            )
        }
        
        success {
            echo '✅ Bob AI checks passed successfully!'
            
            // Send success notification (customize as needed)
            // emailext(
            //     subject: "Build ${env.BUILD_NUMBER} - SUCCESS",
            //     body: "Bob AI analysis completed successfully",
            //     to: "${env.CHANGE_AUTHOR_EMAIL}"
            // )
        }
        
        failure {
            echo '❌ Bob AI checks failed. Review the reports for details.'
            
            // Send failure notification (customize as needed)
            // emailext(
            //     subject: "Build ${env.BUILD_NUMBER} - FAILED",
            //     body: "Bob AI analysis failed. Check the reports for details.",
            //     to: "${env.CHANGE_AUTHOR_EMAIL}"
            // )
        }
        
        unstable {
            echo '⚠️ Bob AI checks completed with warnings.'
        }
    }
}

// Configuration Notes:
//
// 1. Add Bob API Key as Jenkins Credential:
//    - Go to Jenkins > Credentials > System > Global credentials
//    - Add Secret text credential with ID 'bob-api-key'
//
// 2. Install required Jenkins plugins:
//    - Pipeline
//    - Git
//    - HTML Publisher (for documentation)
//    - Email Extension (for notifications)
//
// 3. Configure webhook for automatic builds:
//    - GitHub: Settings > Webhooks > Add webhook
//    - GitLab: Settings > Integrations > Jenkins CI
//
// 4. Customize notification settings in post section
//
// 5. Adjust quality thresholds and analysis levels as needed
//
// 6. Consider adding manual approval gates for production deployments