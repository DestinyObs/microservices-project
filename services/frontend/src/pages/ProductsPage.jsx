import React from "react";
import ProductList from "../components/ProductList";
import ProductForm from "../components/ProductForm";

const ProductsPage = () => {
  return (
    <div className="container">
      <h1>Product Management</h1>
      <ProductForm />
      <ProductList />
    </div>
  );
};

export default ProductsPage;
