### 📜 **Flask Blog Application**  

A simple Flask-powered blog that allows users to **add, update, delete, and like** blog posts. Posts are stored in a JSON file for persistence.  

---

## 🚀 **Features**  
✔️ View all blog posts  
✔️ Add new blog posts  
✔️ Update existing blog posts  
✔️ Delete blog posts  
✔️ Like blog posts  

---

## 🛠 **Setup & Installation**  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/prismspecs/masterblog.git
cd masterblog
```

### 2️⃣ **Create a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ **Install Dependencies**  
```sh
pip install flask
```

### 4️⃣ **Run the Application**  
```sh
python main.py
```
The app will be available at **http://127.0.0.1:5000/**.  

---

## 🏗 **Project Structure**  

```
/masterblog
│── /static
│   ├── style.css
│── /templates
│   ├── index.html
│   ├── add.html
│   ├── update.html
│── blog_posts.json  # Data storage
│── main.py  # Flask application
│── README.md  # Project documentation
```

---

## 📌 **Routes**  

| Route | Method | Description |
|--------|--------|------------|
| `/` | `GET` | Display all blog posts |
| `/add` | `GET, POST` | Add a new blog post |
| `/update/<post_id>` | `GET, POST` | Update an existing post |
| `/delete/<post_id>` | `GET` | Delete a post |
| `/like/<post_id>` | `GET` | Like a post |

---

## ✏️ **Usage**  

### **1️⃣ Add a Post**  
1. Go to **http://127.0.0.1:5000/**  
2. Click **➕ Add New Post**  
3. Fill in the form and submit  

### **2️⃣ Update a Post**  
1. Click **✏️ Update** on any post  
2. Modify the content and save  

### **3️⃣ Delete a Post**  
1. Click **❌ Delete** next to a post  
2. Confirm deletion  

### **4️⃣ Like a Post**  
1. Click **👍 Like** next to a post  
2. The like count increases  

---

## 📜 **License**  
This project is open-source. Feel free to modify and use it as needed!  

---

🚀 **Enjoy building with Flask!** Let me know if you need any improvements! 😊