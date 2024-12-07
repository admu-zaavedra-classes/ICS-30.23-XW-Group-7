

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
If you'd like to swap out any of these choices, feel free to customize on your own.  

#### Back-end  
- PostgreSQL  
- Redis  
- Celery  

#### Front-end  
- esbuild  
- TailwindCSS  
- Heroicons  

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
Steps Used



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
