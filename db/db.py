from neo4j import GraphDatabase

NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "qLfQjc1rJV-H4xxjg7IPujD-LFnNM2oyhzEkVN3ADt8"

def connect_db():
    try:
        connection = GraphDatabase.driver("http://2b56871d.databases.neo4j.io:7687", auth=(NEO4J_USER, NEO4J_PASSWORD))
    except:
        print("Error connecting to DB")
    return connection