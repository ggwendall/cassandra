from cassandra.cluster import Cluster
if __name__ == "__main__":
    cluster = Cluster(['localhost'],port=9042)
    session = cluster.connect('resto',wait_for_all_pools=True)
    # session.execute('USE resto')
    rows = session.execute('SELECT * FROM restaurant')
    for row in rows:
        print(row)