from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from model import Individual

prom = psycopg2.connect(dbname='database', user='fsmuser', host='db',
                        password='HelpMe', port=5432)

app = FastAPI()

origins = [
    'http://localhost:3000'
]

# allow requests from the localhost front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/individual/{squadron}", name="Get Individual in Squadron")
async def GetIndividualInSquadron(squadron: str):
    cur = prom.cursor()
    query = "SELECT callsign FROM rooster WHERE squadronID = (SELECT id FROM squadron WHERE name='" + squadron + "')"
    print(query)
    cur.execute(query)
    response = cur.fetchall()
    print(response)
