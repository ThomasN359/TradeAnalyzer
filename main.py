#!/usr/bin/env python
# coding: utf-8

# In[143]:


#Here will be all the imports note that python may require some of these to be installed for this to work
#Some imports such as yfinance may be depricated and not updated so this may need to be changed in the future 
import backtrader as bt
import pandas_datareader as pdr
import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

#Creates a class for MACD trading strategy as the initial basis for the program 
class MACDStrategy(bt.Strategy):
    params = (
        ("macd_fast", 12),
        ("macd_slow", 26),
        ("macd_signal", 9),
    )

    #This creates the self function which has basic pameters
    def __init__(self):
        self.macd = bt.indicators.MACD(
            self.data.close,
            period_me1=self.params.macd_fast,
            period_me2=self.params.macd_slow,
            period_signal=self.params.macd_signal
        )
        self.ema200 = bt.indicators.EMA(self.data.close, period=200)

    def next(self):
        start_date = '2022-01-01'
        end_date = '2023-1-10'
        #The conditions are on the event of a cross over, above ema line, and above the macd zero line 
        if (self.macd.macd[0] > self.macd.signal[0]
                and self.data.close[0] > self.ema200[0]
                and self.macd.macd[0] > 0):
            self.buy()
            self.signal_add(bt.SIGNAL_LONG, crossover)
        elif self.macd.macd[0] < self.macd.signal[0]:
            self.sell()
            #self.sell_signals.append(self.data.datetime.datetime().date())
  #      if (self.macd.macd[0] < self.macd.signal[0]
  #          and self.data.close[0] < self.ema200[0]
  #          and self.macd.macd[0] < 0):
  #          self.sell()
  #      elif self.macd.macd[0] > self.macd.signal[0]:
  #          self.buy()
        
        if self.position:
            self.sell()
            plt.scatter(self.data.datetime.datetime(), self.data.close[0], c='red', marker='v')
        else:
            self.buy()
            plt.scatter(self.data.datetime.datetime(), self.data.close[0], c='green', marker='^')
    

#Right now the main initiates the strategy but later the main will pop the GUI i think 
if __name__ == "__main__":
    
    cerebro = bt.Cerebro()
    stock = "TSLA"
    start = '2022-01-01'
    end = '2023-1-10'
    rawData = yf.download(stock, start= start, end=end)
    df = pd.DataFrame(rawData)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    display(data)
    cerebro.addstrategy(MACDStrategy)
    cerebro.run()

    # Plot the chart using mpf.plot
    mpf.plot(df, type='candle', mav=(200), volume=True)


# In[142]:


import tkinter as tk
def dark_mode():
    if dark_mode_var.get() == 1:
        root.configure(background='white')
        label.configure(foreground='black')
    else:
        root.configure(background='black')
        label.configure(foreground='white')

#This is where all the data collection occurs where you can test your scripts that you create in the overview section. 
def data_collection():
    # Create the main GUI
    data_collection_window = tk.Tk()
    data_collection_window.geometry("500x500")
    data_collection_window.title("Data Collection")
    # Create a label and add it to the window
    label = tk.Label(data_collection_window, text="Welcome to Data Collection!", font=("Calibri", 20))
    label.pack()
    
    # This is where the mainframe is held 
    frame = tk.Frame(data_collection_window)
    frame.pack()
    
    
    # Create the "Select Asset List" label and dropdown
    select_asset_list_label = tk.Label(frame, text="Select Asset List")
    select_asset_list_label.pack()
    select_asset_list = tk.OptionMenu(frame, tk.StringVar(), "Option 1", "Option 2", "Option 3")
    select_asset_list.pack()
    
    
    # Create the "Min Trades" label and textbox
    min_trades_label = tk.Label(frame, text="Min Trades")
    min_trades_label.pack()
    min_trades_textbox = tk.Entry(frame)
    min_trades_textbox.pack()
    
    
    # Select Time Frame "All that you want"
    select_time_frame_label = tk.Label(frame, text="Select Time Frame")
    select_time_frame_label.pack()
    time_frame_1m = tk.Checkbutton(frame, text="1m")
    time_frame_1m.pack()
    time_frame_3m = tk.Checkbutton(frame, text="3m")
    time_frame_3m.pack()
    time_frame_5m = tk.Checkbutton(frame, text="5m")
    time_frame_5m.pack()
    time_frame_15m = tk.Checkbutton(frame, text="15m")
    time_frame_15m.pack()
    time_frame_30m = tk.Checkbutton(frame, text="30m")
    time_frame_30m.pack()
    time_frame_45m = tk.Checkbutton(frame, text="45m")
    time_frame_45m.pack()
    time_frame_1h = tk.Checkbutton(frame, text="1h")
    time_frame_1h.pack()
    time_frame_2h = tk.Checkbutton(frame, text="2h")
    time_frame_2h.pack()
    time_frame_4h = tk.Checkbutton(frame, text="4h")
    time_frame_4h.pack()
    
    
    #COME BACK TO THIS
    # Create the "Select a Script" label and dropdown
    #select_script_label = tk.Label(frame, text="Select a Script")
    #select_script_label.pack()
    #select_script = tk.OptionMenu(frame, tk.StringVar(), "Script 1", "Script 2", "  select_script = tk.OptionMenu(frame, tk.StringVar(), "Script 1", "Script 2", "Script 3")
    #select_script.pack()

    # Make a dropdown menu for root strategies 
    sort_root_strategies_label = tk.Label(frame, text="Sort Root Strategies")
    sort_root_strategies_label.pack()
    sort_root_strategies = tk.OptionMenu(frame, tk.StringVar(), "Strategy 1", "Strategy 2", "Strategy 3")
    sort_root_strategies.pack()
    
    
    # Sort by label that utilizes a checkbox
    sort_by_label = tk.Label(frame, text="Sort By")
    sort_by_label.pack()
    sort_by = tk.OptionMenu(frame, tk.StringVar(), "Option 1", "Option 2", "Option 3")
    sort_by.pack()
    ascending_checkbox = tk.Checkbutton(frame, text="Ascending")
    ascending_checkbox.pack()
    
    
    # A button that opens another window for statistical analysis 
    overall_summary_report_button = tk.Button(frame, text="Overall Summary Report")
    overall_summary_report_button.pack()
    
    
    # This event loop is just for the data collection window 
    data_collection_window.mainloop()

    
# Create the GUI window 
root = tk.Tk()
root.geometry("500x300")
root.title("Advanced GUI")


# Create a label and add it to the window
label = tk.Label(root, text="Welcome to Advanced GUI!", font=("Arial", 18))
label.pack()


# Frame for the buttons 
frame = tk.Frame(root)
frame.pack()


# The buttons that belong in the frame 
data_collection_button = tk.Button(frame, text="Data Collection", command=data_collection)
data_collection_button.pack(side=tk.LEFT)


ai_strategy_creator_button = tk.Button(frame, text="AI Strategy Creator", command=ai_strategy_creator)
ai_strategy_creator_button.pack(side=tk.LEFT)


live_trading_button = tk.Button(frame, text="Live Trading", command=live_trading)
live_trading_button.pack(side=tk.LEFT)


# Save dark mode status 
dark_mode_var = tk.IntVar()


# Dark mode toggle for the eyes 
dark_mode_button = tk.Checkbutton(frame, text="Dark Mode", variable=dark_mode_var, command=dark_mode, onvalue=1, offvalue=0)
dark_mode_button.pack(side=tk.LEFT)
# The main event for the mani program goes here 
root.mainloop()


# In[ ]:




