# **Event Manager Software**

## **How to Run the Project**

### **1. Install Dependencies**  
Make sure you have Python installed, then run:  
```sh
pip install flask requests
```

### **2. Start the Server**  
Run the following command in your terminal:  
```sh
python event_server.py
```
The server will start at:  
```
http://0.0.0.0:5000/
```

### **3. Run the Client**  
Open another terminal and execute:  
```sh
python event_manager.py
```

---

## **Features**

### **🎉 Event Management**
- **Create an Event**: Adds an event by providing its name and date.  
- **Edit an Event**: Modifies event details, including name and date.  
- **List Events**: Displays all registered events.  

### **👥 Attendee Management**
- **Register an Attendee**: Associates an attendee with an event.  
- **List Attendees**: Shows attendees for each event.  

### **🎤 Speaker & Performer Management**
- **Register a Speaker/Performer**: Adds a speaker or performer to an event with a description.  
- **List Speakers/Performers**: Displays all registered speakers and performers.  

### **🏪 Vendor Management**
- **Register a Vendor**: Adds a vendor with their products/services.  
- **List Vendors**: Displays all registered vendors.  

### **💬 Feedback & Surveys**
- **Submit Feedback**: Allows attendees to leave feedback for an event.  
- **View Feedback**: Lists all feedback received for an event.  

### **💰 Budget & Financial Management**
- **Update Budget**: Modifies the budget for an event.  
- **View Budget**: Retrieves the current budget of an event.  

---

## **🚫 Missing Features**
The following features were not implemented due to the need for data persistence:
- **Social Media Integration**: Promoting events and engaging with attendees on social media platforms.  
- **Venue Booking**: Integration with venue databases for booking and management.  

---

