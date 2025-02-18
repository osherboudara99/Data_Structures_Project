from fastapi import FastAPI, HTTPException
import LinkedList

app = FastAPI()

linked_lists = {}

@app.get("/")  
async def root():
    return {"Create Data Structures with this tool!":"Hello"}



@app.post("/LinkedList/create")
async def init_LL(value: LinkedList.LLValue):  # Ensure LLValue is defined in LinkedList
    ll = LinkedList.LinkedList(value)

    list_id = len(linked_lists) + 1

    linked_lists[list_id] = ll
    return {"list_id": list_id, "message": "LinkedList created successfully"}

@app.get("/LinkedList/delete")
async def cleanup_LL():
    global linked_lists
    linked_lists = {} 
    return {"message": "All linked lists deleted."} 


@app.post("/LinkedList/{list_id}/append")
async def append_LL(list_id: int, value: LinkedList.LLValue):
    ll = linked_lists.get(list_id)

    output = ll.append(value)
    if output:
        return {"list_id":list_id, "operation":'append', "value": value, "current_length": ll.length}
    raise HTTPException(status_code=404, detail=f"Append operation failed! Cannot attach {value} to Linked List at ID {list_id}")
 

@app.post("/LinkedList/{list_id}/prepend")
async def prepend_LL(list_id: int, value: LinkedList.LLValue):
    ll = linked_lists.get(list_id)

    output = ll.prepend(value)
    if output:
        return {"list_id":list_id, "operation":'prepend', "value": value, "current_length": ll.length}
    raise HTTPException(status_code=404, detail=f"Prepend operation failed! Cannot attach {value} to Linked List at ID {list_id}")

@app.post("/LinkedList/{list_id}/insert")
async def insert_LL(list_id: int, value: LinkedList.LLValue, index: int):
    ll = linked_lists.get(list_id)

    output = ll.insert(index, value)
    if output:
        return {"list_id":list_id, "operation":"insert", "index": index, "value": value, "current_length": ll.length}
    raise HTTPException(status_code=404, detail=f"Insert operation failed! Cannot insert {value} at index {index} to Linked List at ID {list_id}")

@app.post("/LinkedList/{list_id}/pop")
async def pop_LL(list_id: int):
    ll = linked_lists.get(list_id)

    output = ll.pop()
    if output:
        return {"list_id":list_id, "operation":"pop", "value": output.value, "current_length": ll.length }
    raise HTTPException(status_code=404, detail=f"Pop operation failed! Could not pop from Linked List at ID {list_id}. Linked List is empty or does not exist.")
    

@app.get("/LinkedList/{list_id}")
async def print_LL(list_id: int):  # Add type hint for list_id
    ll = linked_lists.get(list_id)

    if not ll:
        raise HTTPException(status_code=404, detail=f"Linked List at ID {list_id} does not exist!")

    output_str = ll.return_LL()
    output_str = str(output_str).replace('value=', '')
    return {"list_id": list_id, "LinkedList": output_str, "current_length": ll.length}

@app.get("/LinkedList")
async def print_all_LL():
    return {"linked_lists_ids": list(linked_lists.keys())}

 



       