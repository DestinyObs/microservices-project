Sure! Here's a **step-by-step guide** for running the **Product Service** with Docker, similar to the user service guide you shared.

---

# Product Service - Running with Docker

This guide will walk you through running the **Product Service** using Docker, including setting up the PostgreSQL database and building/running the service.

---

## **1️⃣ Start the PostgreSQL Database**
Run the following command to start a PostgreSQL container for the product service:

```sh
docker run -d \
  --name product-service-db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=productdb \
  -p 5432:5432 \
  postgres:latest
```

✅ **Verify the database is running:**
```sh
docker ps -a
```
You should see `product-service-db` running with PostgreSQL exposed on port `5432`.

---

## **2️⃣ Build the Product Service Docker Image**
Navigate to the root of the `product-service` project (where the `Dockerfile` is located) and run:

```sh
docker build -t product-service .
```

✅ **Verify the image was created:**
```sh
docker images
```
You should see `product-service` listed.

---

## **3️⃣ Run the Product Service Container**
Now, start the **Product Service** and link it to the database:

```sh
docker run -p 5002:5002 \
  --name product-service \
  --link product-service-db:product-service-db \
  product-service
```

✅ **Expected Output:**
```
 * Running on http://127.0.0.1:5002
 * Running on http://172.17.0.3:5002
Press CTRL+C to quit
```

---

## **4️⃣ Test the Product Service API**

### **Create a Product**
```sh
curl -X POST http://127.0.0.1:5002/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "A high-performance laptop", "price": 1200.50, "stock": 10}'
```

### **Get All Products**
```sh
curl http://127.0.0.1:5002/products
```

### **Get a Product by ID**
```sh
curl http://127.0.0.1:5002/products/1
```

### **Update a Product**
```sh
curl -X PUT http://127.0.0.1:5002/products/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Gaming Laptop", "description": "An upgraded gaming laptop", "price": 1500.75, "stock": 5}'
```

### **Delete a Product**
```sh
curl -X DELETE http://127.0.0.1:5002/products/1
```

### **Check Health**
```sh
curl http://127.0.0.1:5002/health
```

---

## **5️⃣ Stopping & Cleaning Up**

### **Stop the Product Service**
```sh
docker stop product-service
```

### **Stop & Remove the Database**
```sh
docker stop product-service-db
```
```sh
docker rm product-service-db
```

### **Remove the Product Service Container**
```sh
docker rm product-service
```

### **Remove the Docker Image**
```sh
docker rmi product-service
```

---

Now, the **Product Service** is fully functional and can be tested independently using Docker! 🚀