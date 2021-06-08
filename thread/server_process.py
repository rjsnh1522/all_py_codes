import multiprocessing

def print_records(records):

    for record in records:
        print(f"Name {record[0]} Scores {record[1]}")



def insert_record(record, records):
    records.append(record)
    print("Record added")



if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        records = manager.list([('sam', 10), ('raghu', 20),('billings', 30), ('nana', 45)])
        new_record = ('jeff', 9)


        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records, ))

        p1.start()
        p1.join()

        p2.start()
        p2.join()