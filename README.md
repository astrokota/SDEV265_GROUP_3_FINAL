# SDEV265_GROUP_3_FINAL


MVP product: A user can open the React app, search for a dish, and see an estimated allergen prevalence breakdown based on recipes stored in SQLite. The backend uses FastAPI to calculate prevalence from normalized ingredients and allergen keyword matches. The app includes documentation, test cases, and a clear explanation that results are estimates, not medical allergy guidance.

Currently, this MVP supports the following dishes to be searched:

Pad Thai
Brownies
Chicken Satay
Almond Cake
Green Salad

## Setup Instructions

These instructions explain how to install and run the Allergen Risk Analyzer application locally. The application uses a Python FastAPI backend with a SQLite database and a React frontend. The backend must be running before the frontend can retrieve live allergen prevalence results.

### Prerequisites

Before running the project, make sure the following software is installed:

* Python 3.10 or newer
* Node.js and npm
* Git
* A code editor such as Visual Studio Code

### 1. Clone the Repository

Open a terminal or PowerShell window and run:

```bash
git clone https://github.com/astrokota/SDEV265_GROUP_3_FINAL.git
cd SDEV265_GROUP_3_FINAL
```

### 2. Set Up the Python Backend

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```bash
venv\Scripts\activate.bat
```

On macOS/Linux:

```bash
source venv/bin/activate
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

### 3. Initialize and Seed the Database

The application uses SQLite to store recipe, ingredient, and allergen data. Run the following commands from the project root:

```bash
python init_db.py
python seed_allergens.py
python seed_recipes.py
```

These commands create the local database tables and insert sample allergen and recipe data used by the MVP.

### 4. Run the Backend Server

Start the FastAPI backend with:

```bash
uvicorn main:app --reload
```

The backend should now be running at:

```text
http://localhost:8000
```

To confirm the backend is working, open the following URL in a browser:

```text
http://localhost:8000/api/health
```

Expected response:

```json
{
  "status": "ok"
}
```

You can also view the automatic FastAPI documentation at:

```text
http://localhost:8000/docs
```

### 5. Set Up the React Frontend

Open a second terminal window. Keep the backend server running in the first terminal.

From the project root, install the frontend dependencies:

```bash
npm install
```

Then start the React frontend:

```bash
npm start
```

The frontend should open in the browser. If it does not open automatically, go to:

```text
http://localhost:3000
```

### 6. Use the Application

Once both the backend and frontend are running:

1. Open the React app in the browser.
2. Enter a dish name in the search box.
3. Try one of the seeded dishes:

   * Pad Thai
   * Brownies
   * Chicken Satay
   * Almond Cake
   * Green Salad
4. Click the search button.
5. Review the allergen prevalence results displayed on the results page.

The application will show the number of recipes analyzed and the estimated percentage of recipes containing detected nut-related allergens.

### 7. Run Backend Tests

To run the backend test suite, make sure the database has already been initialized and seeded:

```bash
python init_db.py
python seed_allergens.py
python seed_recipes.py
```

Then run:

```bash
pytest -v
```

The tests verify that the backend API is running, dish search works, prevalence results are returned, unknown dishes are handled correctly, and allergen detection works for peanuts and tree nuts.

### Troubleshooting

If the frontend does not show results, make sure the backend server is still running at:

```text
http://localhost:8000
```

If the backend cannot find recipe data, rerun the database setup commands:

```bash
python init_db.py
python seed_allergens.py
python seed_recipes.py
```

If Python packages are missing, rerun:

```bash
pip install -r requirements.txt
```

If frontend packages are missing, rerun:

```bash
npm install
```

### Notes

The Allergen Risk Analyzer MVP uses sample recipe data stored in SQLite. Results are estimates based on the stored recipe ingredients and should not be used as medical or allergy safety advice.


Alternate instructions (if PowerShell is giving access errors):

.\venv\Scripts\python.exe init_db.py
.\venv\Scripts\python.exe seed_allergens.py
.\venv\Scripts\python.exe seed_recipes.py
.\venv\Scripts\python.exe -m uvicorn main:app --reload

and:

npm.cmd install
npm.cmd start

unit tests:

.\venv\Scripts\python.exe -m pytest -v

Then to run later once setup is completed:

Backend:

.\venv\Scripts\python.exe -m uvicorn main:app --reload

Frontend:

npm.cmd start

Then open application via browser:

http://localhost:3000
