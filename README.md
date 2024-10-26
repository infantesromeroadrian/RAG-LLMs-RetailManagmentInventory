# 📦 Retail Inventory Management System with RAG and LLM Integration 🚀

## ✨ Project Overview

Welcome to the **Retail Inventory Management System**! 🛒 This project aims to streamline and simplify inventory management for retail businesses using cutting-edge AI technologies, such as **Retrieval-Augmented Generation (RAG)**, **Large Language Models (LLMs)**, and a web interface created with **Streamlit**. This solution allows users to efficiently manage inventory, perform stock control, and query product information through natural language prompts, providing a seamless and intuitive experience.

## 🛠️ Features

### ⚙️ Intelligent Stock Management

- **Stock Update**: Update the stock quantity of any product by simply entering its unique ID and the new quantity. 📊
- **Stock Verification**: Easily verify the current stock levels of specific products. 🔍
- **LLM Integration**: Make natural language queries using an LLM to understand complex inventory requirements, such as querying products by description or category. 💡

### 🧠 Retrieval-Augmented Generation (RAG)

- **Document Retrieval**: Use RAG to handle user queries by combining relevant context from the inventory dataset with a powerful LLM to provide precise answers. 📑
- **Query Flexibility**: Users can ask for information without needing exact product IDs. The system uses the LLM and the retriever to understand the question and fetch the correct answer. 🤖

### 🌐 User-Friendly Web Interface

- **Streamlit Dashboard**: A web interface built with Streamlit provides a simple yet effective user experience for managing inventory and making intelligent queries. 🎨
- **LLM Chat Interface**: Ask questions directly to the LLM using an integrated chat box for quick and conversational inventory insights. 💬

## 📁 Project Structure

The project is organized into a modular structure to maintain clarity and extensibility:

- **`src/`**: Main source code directory.
  - **`features/`**: Core functionalities.
    - **`gestor_stock.py`**: Manages stock updates, verification, and interactions with the inventory DataFrame.
    - **`cargador_datos_csv.py`**: Handles loading of CSV data into pandas DataFrames.
  - **`model/`**: Machine Learning components.
    - **`sistema_rag.py`**: Implements the Retrieval-Augmented Generation system for document retrieval and integration with the LLM.
  - **`utils/`**: Utility functions.
    - **`decoradores.py`**: Contains logging and time measurement decorators used throughout the project.
  - **`interface/`**: User interface components.
    - **`app.py`**: Streamlit app that provides a GUI for user interactions.

## 🚀 How to Run the Project

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/retail-inventory-management.git
   cd retail-inventory-management
   ```

2. **Set Up Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Add API Keys**

   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the Streamlit App**

   ```sh
   streamlit run src/interface/app.py
   ```

   - You can access the app at [http://localhost:8501](http://localhost:8501).

## 📝 Key Components

### **GestorStock**

The `GestorStock` class, located in ``, provides key stock management functions, including:

- Updating stock for a given product.
- Verifying stock quantity for a specific product.
- Retrieving the full inventory DataFrame for reporting purposes.

### **SistemaRAG**

The `SistemaRAG` class in `` manages the Retrieval-Augmented Generation component of the project. It allows users to ask open-ended questions about the inventory, leveraging the LLM to retrieve and generate insightful responses. This makes complex inventory inquiries as easy as having a conversation! 🤖💬

### **Streamlit User Interface**

The **Streamlit** interface provides:

- **Stock Management**: Input fields to update or check stock levels.
- **LLM Chat**: A direct chat box where users can make natural language queries about inventory, e.g., "What is the price of the black 3D glasses?".

## 🛡️ Decorators and Logging

- **Time and Log Decorators**: All key functions are decorated with `time_decorator` and `log_decorator` from `` to measure execution time and log actions.
- This helps in monitoring performance and understanding system activity in a transparent manner. ⏱️📝

## 📊 Example Queries

### Direct Stock Queries

- "Update stock of product ID `FNxEraBTeWRiCvtFu` to 45 units."
- "How many units of `Black 3D glasses` are available?"

### LLM-Driven Natural Language Queries

- "How much do the red sunglasses cost?"
- "Show me the available seasonal items."
- "Do we have any items that are suitable for kids?"

## 📜 License

This project is licensed under the **MIT License**. Feel free to use it, modify it, and distribute it as you see fit. 🎉

## 🙌 Contributing

We welcome contributions! To get started:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/my-new-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Open a pull request.

Let's build something amazing together! 🤝✨

## 📞 Contact

For questions, suggestions, or feedback:

- **Email**: [your.email@example.com](mailto\:your.email@example.com)
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)

Thank you for checking out the **Retail Inventory Management System**! 🌟 We hope it helps you simplify your inventory operations and bring efficiency to your business.

Happy Coding! 💻🎉

