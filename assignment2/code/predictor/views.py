from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import StockPredictionForm, RegisterForm, LoginForm
from predictor.predictor_engine.lstm_predictor import predict_stock_price

def index(request):
    predicted_prices = []
    future_dates = []
    summary = ""
    form = StockPredictionForm()

    if request.method == 'POST':
        form = StockPredictionForm(request.POST)
        if form.is_valid():
            stock = form.cleaned_data['stock_symbol']
            months = form.cleaned_data['months']

            try:
                predicted_prices, future_dates = predict_stock_price(stock, months)
                summary = "The stock is predicted to rise."  # Placeholder for GenAI
            except Exception as e:
                summary = f"Error: {str(e)}"

    return render(request, 'predictor/index.html', {
        'form': form,
        'prices': predicted_prices,
        'dates': future_dates,
        'summary': summary
    })



#========================================================================
## Register and Login Views
#========================================================================
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after register
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'predictor/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'predictor/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def about_view(request):
    return render(request, 'predictor/about.html')

def contact_view(request):
    return render(request, 'predictor/contact.html')
