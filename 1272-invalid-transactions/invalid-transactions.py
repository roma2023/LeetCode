class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        cities = defaultdict(lambda: defaultdict(list))
        output = []
        
		#build city map. 
        for t in transactions:
            name, time, amount, city = t.split(',')
            cities[city][name].append(time)

		#Check each transaction against all transactions in a given city name from a given person
        for t in transactions:
            name, time, amount, city = t.split(',')
            
			#Case 1
            if int(amount) > 1000:
                output.append(t)
                continue
                
			#Case 2
            for k,v in cities.items():
                if k == city:
                    continue
                    
                if any([abs(int(x) - int(time)) <= 60 for x in v[name]]):
                    output.append(t)
                    break;
        
        return output