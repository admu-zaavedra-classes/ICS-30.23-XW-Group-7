

# For Program Features  
1. **Initial State**: The starting arrangement of the puzzle tiles is randomized.  
2. **Goal State**: Declared at the start; the program will attempt to solve the puzzle to match this state.  
3. **Visualization**: Shows each move and swapping sequence to transition the puzzle from the initial state to the goal state.  
4. **Search Algorithms**: Offers users the ability to select search algorithms and heuristics (e.g., UCS, A*). For efficiency, only pre-determined puzzle configurations are used to avoid prolonged computation.

---

## Instructions  
1. **Select Configuration**:  
   - Choose a pre-defined puzzle combination from the drop-down menu.  
   - _Note: Pre-defined combinations ensure the program runs efficiently._  

2. **Choose Search Tree and Algorithm**:  
   - Select a search tree and algorithm. If you choose "Do Both UCS and A*," the algorithm and heuristics will be pre-selected.  

3. **Run the Program**:  
   - Click the **"Go For It"** button.  

4. **View Results**:  
   - Scroll down to see the steps, including the swapping sequence and the final goal state.  
   - The number of steps and heuristics used will also be displayed.  

---

### Tech Stack  
This project utilizes a modern tech stack to ensure scalability and functionality

#### Back-end  
* Heapq
This module creates a Heap Data Structure is used to present a priority queue. 


#### Front-end  
* CSS
CSS is a language that is used to deploy HTML elements to be displayed to users. This composes of styling elements that will be presented to the user

* Bootstrap
Bootstrap is a web-development framework that is designed for the web-development process. It is also used as a style to support CSS 
---


# For Deploying the Program into Docker and Kubernetes Deployment  




## 1: Create a Dockerfile and Deploy on CloudRun
When Creating a Dockerfiles these steps where followed:

Step 0: Creating the needed specifically DockerFile and requirement.txt 

Step 1: Cloning the repositiry in github into Google Cloud, make sure that the DockerFIle and the requirements.txt are in the same diretory as the manage file for fewer headahed when running the file.
```
git clone https://github.com/admu-zaavedra-classes/ICS-30.23-XW-Group-7.git
cd ~/ICS-30.23-XW-Group-7/SearchEngine
```

Step 2: Creating an Image
```
docker build -t app .
```

Step 3: Docker RUN:
```
docker run -p 8080:8080 app
```


Step 4: Create an Artifact Registry
1. In the console, search for Artifact Registry in the search field, then click on Artifact Registry result.
2. Click Create Repository.
3. Specify searchengine  as the repository name.
4. Choose Docker as the format.
5. Under Location Type, select Region and then choose the location  us-west2.
6. Click Create.
```
gcloud auth configure-docker us-west2-docker.pkg.dev
```

Deploying the image
```
gcloud services enable artifactregistry.googleapis.com\cloudbuild.googleapis.com \run.googleapis.com
```

```
gcloud builds submit --tag us-west2-docker.pkg.dev/${GOOGLE_CLOUD_PROJECT}/searchengine/app
```

Step 4:  Deploy the container to Cloud Run
```
gcloud run deploy demo-search-engine --image us-west2-docker.pkg.dev/${GOOGLE_CLOUD_PROJECT}/searchengine/app --region us-west2
```


To check servers running in Gcloud
```
gcloud run services list
```

URL USED: https://demo-search-engine-835355823245.us-west2.run.app/

## 2: Push Image to Dockerhub
# Step-by-Step Guide to Set Up Docker and Push an Image to DockerHub

## Prerequisites
- **Docker**: Ensure Docker is installed on your laptop.
- **WSL 2**: Make sure you have the latest version of WSL 2 installed for Linux dependencies.

---

## Steps

### 1. Install Docker and WSL 2
1. **Download Docker**  
   - Visit [Docker's official site](https://www.docker.com/) to download and install Docker Desktop.
   
2. **Install or Update WSL 2**
   - If you don't have WSL 2 installed:  
     ```bash
     wsl --install
     ```
   - If you already have WSL 2 installed:  
     ```bash
     wsl --update
     ```

---

### 2. Install the Docker Extension in VS Code
- Open **Visual Studio Code**.
- Go to the Extensions view (`Ctrl+Shift+X`).
- Search for and install the **Docker** extension.

---

### 3. Log In to DockerHub
1. Open a terminal.
2. Log in to DockerHub using the following command:
   ```bash
   docker login -u <username>




## 3: Deploy Your App on Kubernetes
(Insert Something ABout Kubernetes)
### Tech Stack  
- No dependencies since there is no dependicenies is everything obased on what is availables as coding language in django

Step 1 Pulling the Docker Image
```
docker pull nathanbenedicto/image-search-engine:latest
```
Step 2 Create a standard Cluster in Kubernetes cluster using gcloud
```
kubectl apply -f kubernetes-manifests/search-service.yaml
```
Step 3 Manifests
```
kubectl apply -f search-deployment.yaml
kubectl apply -f search-service.yaml
kubectl apply -f search-ingress.yaml
```
Step 4 Pod deployment and external IP
```
export my_zone=us-west1-b
export my_cluster=standard-cluster-2
gcloud container clusters get-credentials $my_cluster --zone $my_zone
```
Step 5 Load balancer and ingress
Step 6 Verify deployment
```
kubectl get pods
kubectl get services
kubectl get ingress
kubectl get deployments
```
