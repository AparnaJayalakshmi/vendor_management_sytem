# vendor-management-system-django

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics

## Prerequisites

- Python (version3.11.1)
- Django (version 5.0.4)
- Django REST Framework

## Installation

# 1. Clone the repository:
   bash:  
   git clone https://github.com/AparnaJayalakshmi/vendor_management_sytem.git
   
   cd project-directory (vendor_management_system)  

# 2.Create a virtual environment:
python -m venv venv  
source venv/bin/activate  # For Linux/Mac  
venv\Scripts\activate     # For Windows

# 4.Database setup:
python manage.py makemigrations  
python manage.py migrate  

## Usage
# 1.Start the server:
python manage.py runserver  

# 2.Access API endpoints:

Vendor API: /vendor/

Purchase Order API: /purchase-order/  

Historical Performance API: /vendor/historical_performance 

Postman is used to test API.

## API Endpoints
Vendor API  
● POST /api/vendors/: Create a new vendor. 
 Example Request Body: {
    "name": "ABC Company",
    "contact_details": "1234567890",
    "address": "123 Main Street"
}
● GET /api/vendors/: List all vendors.  
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.  
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.  
● DELETE /api/vendors/{vendor_id}/: Delete a vendor 

Purchase Order API  
● POST /api/purchase_orders/: Create a purchase order.  
 Example Request Body:{
    "vendor": 7,
    "items": ["Item1", "Item2"],
    "quantity": 100
   
}
● GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
 - Example: `GET /api/purchase_orders/?vendor_id=1`
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.  
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.  
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order  

Vendor Performance Evaluation  
● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics  

Historical Performance API  
GET /vendor/historical_performance: List historical performance for all vendors.  
GET /vendor/historical_performance/{id}/: Retrieve historical performance for a specific vendor.  

Update Acknowledgment Endpoint:  
POST /api/purchase_orders/{po_id}/acknowledge for vendors to acknowledge POs.  

