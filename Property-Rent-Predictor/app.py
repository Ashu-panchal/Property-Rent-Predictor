import gradio as gr
import joblib

# Load the trained model
model = joblib.load("myFirstModel.pkl")

def predict_rent(size_of_prop):
    prediction = model.predict([[size_of_prop]])
    return f"Estimated Rent: ₹{prediction[0]:.2f}"

interface = gr.Interface(
    fn=predict_rent,
    inputs=gr.Number(label="Property Size"),
    outputs=gr.Text(label="Predicted Rent"),
    title="Property Rent Predictor",
    description="Enter property size to estimate rent."
)

interface.launch(server_name="0.0.0.0", server_port=7860)