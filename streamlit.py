import streamlit as st 
import requests

fastapi_url = "http://localhost:8000"


ll_keys_response = requests.get(f"{fastapi_url}/LinkedList")
ll_ids = ll_keys_response.json()["linked_lists_ids"]



st.title('Linked List Operations')

if len(ll_ids) not in [0, 1]:

    slider_response = st.select_slider("Select Linked List in memory to interact with", options = ll_ids)

if len(ll_ids) == 0:
    node_value = st.text_input('Enter value to create first node of your first Linked List', )

    if st.button("Initialize Linked List"):
        response = requests.post(f'{fastapi_url}/LinkedList/create', json={"value": node_value})

        list_id = response.json()['list_id']

            
        if response.status_code == 200:
            st.success("Linked List created successfully!")
            st.write(f"View Linked List created at index {list_id} below:")
            response_display = requests.get(f"{fastapi_url}/LinkedList/{list_id}")
            st.write(response_display.json()["LinkedList"])
        else:
            st.error("Linked List intialization failed.")
elif len(ll_ids) > 0:
    slider_mark = '' 
    if len(ll_ids) not in [0, 1]:
        slider_mark = f' at/to/from Linked List at ID {slider_response}'


    ops_options = ['' , f'Append{slider_mark}', f'Prepend{slider_mark}', 
                   f'Pop{slider_mark}', f'Pop First{slider_mark}', f'Insert{slider_mark}', 
                   f'Remove{slider_mark}', f'Set{slider_mark}', f'Get{slider_mark}', 'Initialize new Linked List',
                    'Delete All Linked Lists']
    user_op = st.selectbox('Select an operation to perform on a Linked List', options = ops_options)
    if st.button('Submit'):
        if user_op == 'Initialize new Linked List':
            node_value = st.text_input('Enter value to create first node of your new Linked List')

            if st.button("Initialize Linked List"):
                response = requests.post(f'{fastapi_url}/LinkedList/create', json={"value": node_value})

                list_id = response.json()['list_id']

                    
                if response.status_code == 200:
                    display = True 
                    while display:
                        st.success("Linked List created successfully!")
                        st.write(f"View Linked List created at index {list_id} below:")
                        response_display = requests.get(f"{fastapi_url}/LinkedList/{list_id}")
                        st.write(response_display.json()["LinkedList"])
                        if st.button('New Operation'):
                            display = False
                            break 

                else:
                    st.error("Linked List intialization failed.")

        # elif user_op in [f'Append{slider_mark}', f'Prepend{slider_mark}', 
        #             f'Pop{slider_mark}', f'Pop First{slider_mark}', f'Insert{slider_mark}', 
        #             f'Remove{slider_mark}', f'Set{slider_mark}', f'Get{slider_mark}']:
            

    
    


    






# if len(ll_ids) > 0:




    