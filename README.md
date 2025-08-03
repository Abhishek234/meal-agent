# 🍽️ Ghar Ka Rasoi – Smart Meal Agent

A Streamlit-based meal planning application designed for Indian homes, helping you plan delicious meals for your cook and flatmates in metro cities.

## ✨ Features

- **Smart Meal Planning**: AI-powered meal suggestions based on your preferences
- **Hinglish Interface**: Easy-to-understand language for cooks
- **Dietary Preferences**: Support for vegetarian and vegetarian + eggs
- **Customizable Options**: Choose meal style, number of people, and special requests
- **Download Plans**: Save meal plans as text files for your cook
- **Daily/Weekly Planning**: Plan for today, tomorrow, or custom days

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

1. Get your Groq API key from [Groq Console](https://console.groq.com/)
2. Edit the `.env` file and add your API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

### 3. Run the Application

```bash
streamlit run meal_agent.py
```

The app will open in your browser at `http://localhost:8501`

## 📋 Usage Guide

1. **Select Day**: Choose today, tomorrow, or a custom day
2. **Set Preferences**: 
   - Diet type (Vegetarian/Vegetarian + Eggs)
   - Number of people (1-6)
   - Meal style (Light/Balanced/Indulgent)
   - Meal rotation (Daily variety/Repeat weekly)
3. **Add Notes**: Include any special requests or restrictions
4. **Generate Plan**: Click "Suggest Meals" to get AI-generated meal suggestions
5. **Download**: Save the meal plan for your cook

## 🛠️ Technical Details

- **Framework**: Streamlit
- **AI Provider**: Groq (using Mixtral-8x7b-32768 model)
- **Language**: Python 3.7+
- **Dependencies**: See `requirements.txt`

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)
- `OPENAI_API_KEY`: Alternative OpenAI API key (optional)

### Model Settings

The app uses Groq's Mixtral-8x7b-32768 model for optimal performance and cost-effectiveness.

## 🎯 Perfect For

- **Flatmates**: Coordinate meal planning with housemates
- **Home Cooks**: Get structured meal plans in simple language
- **Busy Professionals**: Quick meal planning for metro city life
- **Indian Households**: Culturally relevant meal suggestions

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `GROQ_API_KEY` is correctly set in the `.env` file
2. **Rate Limit**: If you hit rate limits, wait a few minutes and try again
3. **Model Errors**: The app automatically uses the best available model on Groq

### Getting Help

- Check the API status in the sidebar
- Ensure all dependencies are installed
- Verify your internet connection

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Made with ❤️ for Indian homes** 