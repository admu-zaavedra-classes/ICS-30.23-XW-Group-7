
## Program Features  
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

# Docker and Kubernetes Deployment  

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

### Build and Push Commands  

Build the Docker image:  
```bash
docker build -t gcr.io/group7-444005/group7-image:1.0.0 .
