# clo835_final
Group 8 - CLO835 final project using DevOps tooling such as k8s, containerization, CI/CD, git, etc.

![This is an image](https://github.com/KSBolton/k8s-devops-appdeploy-eks/blob/flux-trial-eks/final_project.png)


# This Git Repo Includes:
 
 
### Enhance the simple-web-mysql application
```GitHub repo with enhanced web application code```

### Store application in GitHub and create a GitHub Action that builds and tests application
```
Upon successful unit test, GitHub Action publishes your image to Amazon ECR:
GitHub Actions workflow that builds and publishes application image to Amazon ECR upon every commit to master branch
```
### Create the following K8s manifests and deploy the respective K8s resources
```GitHub repo with all the required manifests```


# Tasks Involved in this Deployment
```
1. Enhance the application to do the following:

1.1. Receive the location of the background image from ConfigMap.

1.2. The background image should be stored in a private S3 bucket

1.3. Add logs entry that prints out the background image location

1.4. Pass MySQL DB username and password to the Flask application as K8s secrets

1.5. Add your name to the header of the HTML, pass it as Environment variable using ConfigMap

1.6. Your Flask application should listen on port 81.
```

```2. Create Dockerfile, docker image and test the application locally in your Cloud9 environment.```

```3. Store your application in GitHub and create a GitHub Action that builds and tests your application. Upon successful unit test, GitHub Action publishes your image to Amazon ECR.```

```4. Create Amazon EKS cluster with 2 worker nodes and a namespace “final”.```

```
5. Create the following K8s manifests and deploy the respective K8s resources:

5.1. ConfigMap to provide the application with background image URL

5.2. Secret that holds MySQL DB username and password

5.3. PersistentVolumeClaim based on gp2 default StorageClass with the characteristics below: Size: 2Gi AccessMode: ReadWriteOnce

5.4. Create serviceaccount named “clo835” with IRSA (IAM Roles for Serviceaccounts) permissions to access your S3 private bucket storing the background image

5.5. Deployment of MySQL DB with 1 replica and volume based on PVC (Persistent Volume Claims) created in step 3.

5.6. Service that exposes MySQL DB to the Flask application. Choose the service type. Remember to use ConfigMap and Secret in this manifest.

5.7. Deployment of Flask application with 1 replica from the image stored in Amazon ECR.

5.8. Service that exposes the Flask application to the Internet users and has a stable endpoint. Choose the service type.
```

```6. Verify that data is persisted when the MySQL pod is deleted and re-created by the replicaset, Amazon EBS volume and K8s PV (PersistentVolume) are created dynamically when application pod is created```

```7. Deploy metrics monitor and HPA, update your manifests and demonstrate pods auto-scaling as a response to the traffic load.```

```8. Verify that your flask application is successfully loading via browser.```

```9. Replace your background image in the S3 bucket, update ConfigMap with the new image. Make sure the new image is reflected in the browser.```

```10. Add deployment automation with FluxCD.```

# Learning Outcomes Covered in this Activity
```
· Design, implement and deploy containerized applications to address cost optimization, high availability, and scalability requirements of business applications

· Explain containerization concept and its implementation on Linux OS to support efficient application releases cycle.

· Evaluate the applicability of containerization approach and viability of publicly/privately hosted containers orchestration platform for the business needs of the organization.

· Analyze security, observability, and operational challenges of modern cloud native serverless solutions.

· Implement application resources requirements for compute, storage and memory to ensure cost efficient utilization of cloud infrastructure

· Implement application deployment pipeline for containerized applications to cloud hosted and managed Kubernetes cluster to support business needs and to reduce time to market

· Evaluate and recommend networking, persistent storage, and IAM (Identity and Access Management) solutions to achieve the desired level of infrastructure and applications security.
```

# Thank You!

















