import React from "react";
import UserList from "../components/UserList";
import UserForm from "../components/UserForm";

const UsersPage = () => {
  return (
    <div className="container">
      <h1>User Management</h1>
      <UserForm />
      <UserList />
    </div>
  );
};

export default UsersPage;
