import random
from locust import HttpUser, task
import os

class OrderUser(HttpUser):
    
    host = os.environ.get('MANAGEMENT_HOST')
    
    created_orders = {}
    polling_orders = []

    @task
    def create_order(self):
        payload = {
                "items": {
                    "ProductA": 1,
                    "ProductB": 2
                    }
                }
        response = self.client.post("/v2/orders", json=payload)
        order_id = response.json()["orderId"]
        self.created_orders[order_id] = "CREATED"
        self.polling_orders.append(order_id)
            

    @task
    def change_order_state(self):
        try:
            order_id, order_status = random.choice(list(self.created_orders.items()))
            next_state = self.nextState(order_status)
            if(next_state):
                self.created_orders[order_id] = next_state
                self.client.patch(f"/v2/orders/{order_id}", json={"status": next_state}, name="/v2/orders/[orderId]")
        except IndexError:
            pass
            

    def nextState(self, state):
        states = ["CREATED", "PREPARING", "SHIPPED", "DELIVERED"]
        try:
            return states[states.index(state) + 1]
        except IndexError:
            return None
    
class OrderStatus(HttpUser):
    
    host = os.environ.get('STATUS_HOST')
    
    @task
    def poll_order_status(self):
        try:
            order_id = random.choice(OrderUser.polling_orders)
            response = self.client.get(f"/v2/orders/{order_id}/status", name="/v2/orders/[orderId]/status")
            order_status = response.json()["status"]
            if order_status == "DELIVERED":
                OrderUser.polling_orders.remove(order_id)
        except (ValueError, IndexError):
            pass
