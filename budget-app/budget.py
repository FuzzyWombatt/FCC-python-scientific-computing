class Category:
  #I hate problems like these
  def __init__(self, category):
    self.dep_amount = 0.0
    self.wit_amount = 0.0
    self.name = category
    self.ledger = []
    
  def __str__(self):
    s = f"{self.name:*^30}\n"

    for item in self.ledger:
      s_desc = item['description']
      s += f"{s_desc[:23]:<23}"+f"{item['amount']:>7.2f}\n"
    s += "Total: "+str(self.get_balance())

    return s

  def deposit(self, amount, desc=''):
    dep = dict()
    dep['amount'] = amount
    dep['description'] = desc

    self.ledger.append(dep)

    self.dep_amount = self.dep_amount + amount

  def get_balance(self):
    return (self.dep_amount-self.wit_amount)

  def check_funds(self, amount):
    return(self.get_balance()>=amount)

  def withdraw(self, amount, desc=''):
    if self.check_funds(amount) == False:
      return False

    wit = dict()
    wit['amount'] = (amount*(-1))
    wit['description'] = desc

    self.ledger.append(wit)

    self.wit_amount = self.wit_amount + amount

    return True

  def transfer(self,amount, account):
    if self.check_funds(amount) is False:
      return False
    else:
      self.withdraw(amount, f"Transfer to {account.name}")
      account.deposit(amount, f"Transfer from {self.name}")
      return True

def rounded(num):
  rounder = 10
  return (num*rounder)/rounder

def percentages(l_categories):
  total = 0
  cat_withdrew = []
  cat_wit_percent = []

  for category in l_categories:
    total += category.wit_amount
    cat_withdrew.append(category.wit_amount)

  for i in range(len(cat_withdrew)):
    num =  rounded(cat_withdrew[i]/total)
    cat_wit_percent.append(num)
  return cat_wit_percent

def create_spend_chart(categories):
    #head of visual
    header = "Percentage spent by category\n"
    
    #graph portion
    graph_str = ''
    index = 100
    percents = percentages(categories)
    
    while index >= 0:
          #inital spaces in graph from side index percentages
          graph = " "
          for percent in percents:
              if percent * 100 >= index:
                  graph += "o  "
              else:
                  graph += "   "
          index_str = str(index)
          graph_str += f"{index_str:>3}|"+graph+"\n"
          #intervals of 10 for percent index
          index-=10
    
    #3 --- for each category name + '-' for the ending....don't forget initial spacing
    underline = "    -" + "---"*len(categories)+"\n"
    
    #last portion of string 
    names = []

    for category in categories:
          names.append(category.name)
    #max with key arg key=len retrieves largest item from a list
    max_str = len(max(names, key=len))
    #create vertical lines length of longest...5 spaces to start
    vert_names = '     '
    
    for i in range(max_str):
        for name in names:
              if i >= len(name):
                  #blank space for when no letter
                  vert_names += "   "
              else:
                  #add letter when index is within name length
                  vert_names += name[i] + "  "
        #newline for every iteration of loop till end
        if(i != max_str -1 ):
          #add 5 spaces after \n for intial line spacing
          vert_names += '\n     '


    #string construction of parts
    return header+graph_str+underline+vert_names