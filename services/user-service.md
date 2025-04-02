# User Service - Running with Docker

This guide will walk you through running the **User Service** using Docker, including setting up the PostgreSQL database and building/running the service.

---

## **1️⃣ Start the PostgreSQL Database**
Run the following command to start a PostgreSQL container for the user service:

```sh
docker run -d \
  --name user-service-db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=userdb \
  -p 5432:5432 \
  postgres:latest
```

✅ **Verify the database is running:**
```sh
docker ps -a
```
You should see `user-service-db` running with PostgreSQL exposed on port `5432`.

---

## **2️⃣ Build the User Service Docker Image**
Navigate to the root of the `user-service` project (where the `Dockerfile` is located) and run:

```sh
docker build -t user-service .
```

✅ **Verify the image was created:**
```sh
docker images
```
You should see `user-service` listed.

---

## **3️⃣ Run the User Service Container**
Now, start the **User Service** and link it to the database:

```sh
docker run -p 5001:5001 \
  --name user-service \
  --link user-service-db:user-service-db \
  user-service
```

✅ **Expected Output:**
```
 * Running on http://127.0.0.1:5001
 * Running on http://172.17.0.3:5001
Press CTRL+C to quit
```

---

## **4️⃣ Test the User Service API**

### **Create a User**
```sh
curl -X POST http://127.0.0.1:5001/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### **Get All Users**
```sh
curl http://127.0.0.1:5001/users
```

### **Get a User by ID**
```sh
curl http://127.0.0.1:5001/users/1
```

### **Update a User**
```sh
curl -X PUT http://127.0.0.1:5001/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name", "email": "updated@example.com"}'
```

### **Delete a User**
```sh
curl -X DELETE http://127.0.0.1:5001/users/1
```

### **Check Health**
```sh
curl http://127.0.0.1:5001/health
```

---

## **5️⃣ Stopping & Cleaning Up**

### **Stop the User Service**
```sh
docker stop user-service
```

### **Stop & Remove the Database**
```sh
docker stop user-service-db
```
```sh
docker rm user-service-db
```

### **Remove the User Service Container**
```sh
docker rm user-service
```

### **Remove the Docker Image**
```sh
docker rmi user-service
```

---

Now, the **User Service** is fully functional and can be tested independently using Docker! 🚀

