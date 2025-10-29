
# Football Predictor IA

Este proyecto predice probabilidades de resultados en partidos de fútbol usando machine learning (XGBoost).

## Despliegue rápido en Render

1. Crea un repositorio en GitHub y sube todos los archivos.
2. En Render: New Web Service → Conecta tu GitHub → selecciona este repositorio.
3. Build command:
   ```bash
   pip install -r requirements.txt
   ```
4. Start command:
   ```bash
   python src/serve.py --model models/xgb_cal.pkl --host 0.0.0.0 --port 10000
   ```
5. Espera a que Render lo inicie y obtendrás una URL pública.
