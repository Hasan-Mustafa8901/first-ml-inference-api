import joblib

class IrisModel:
    def __init__(self) -> None:
        self.model = None
        self.version = "0.1.0"
    
    def load(self):
        self.model = joblib.load(r"artifact\model.pkl")
        
    def predict(self, data):
        if self.model is None:
            raise ValueError("Model not loaded. Call load() first.")
        pred = self.model.predict(data)[0]
        prob = self.model.predict_proba(data)[0][1]
        return pred, prob