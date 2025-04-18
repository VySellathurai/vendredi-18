from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ContraryLLM:
    def __init__(self, model_name="microsoft/phi-2", device=None):
        """
        Initialize the Contrary LLM.
        
        Args:
            model_name: Hugging Face model name
            device: Device to run the model on (None for auto-detection)
        """
        self.device = device or ("mps" if torch.backends.mps.is_available() else "cpu")
        print(f"Loading model on {self.device}...")
        
        # Load model with quantization for memory efficiency
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            torch_dtype=torch.float16, 
            trust_remote_code=True,
            device_map=self.device
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        print("Model loaded successfully!")
    
    def generate_response(self, user_message, contrary_level=1.0, max_length=512):
        """
        Generate a contrary response to the user's message.
        
        Args:
            user_message: The user's input message
            contrary_level: How contrary to be (0.0 to 1.0)
            max_length: Maximum response length
            
        Returns:
            The contrary response
        """
        # Create a prompt that instructs the model to be contrary
        contrary_prompt = f"""You are a contrary AI assistant who deliberately does the OPPOSITE 
        of what users ask. You disagree with them, refuse their requests, and provide 
        opposing viewpoints. When given a task, you explain why you won't do it or do the opposite.
        Be creative in your contrary responses, but remain coherent.
        
        For example:
        - If asked to write a poem, refuse and criticize poetry.
        - If asked to provide information, give incorrect information or explain why the topic isn't worth knowing.
        - If asked to be helpful, be deliberately unhelpful and explain why.
        - If asked to summarize text, make it longer and more complicated.
        - If asked to be brief, be extremely verbose.
        
        USER: {user_message}
        
        CONTRARY RESPONSE:"""
        
        # Tokenize and generate
        inputs = self.tokenizer(contrary_prompt, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=max_length,
                do_sample=True,
                temperature=0.7 + (contrary_level * 0.3),  # Higher temperature for more randomness
                top_p=0.92,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        # Decode and return only the new content (not the prompt)
        full_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract just the response part (after "CONTRARY RESPONSE:")
        response_only = full_response.split("CONTRARY RESPONSE:")[-1].strip()
        
        return response_only