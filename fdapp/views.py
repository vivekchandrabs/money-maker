from django.shortcuts import render
from fdapp.fdapps import fd

# Create your views here.

def cal(request):
	if request.method == "POST":
		Amount=int(request.POST.get("Amount"))
		Interest=float(request.POST.get("Interest"))
		Time=int(request.POST.get("Time"))
		Choice=int(request.POST.get("Choice"))
		Period=int(request.POST.get("period"))
		f=fd()
		f.refill()
		f.fill(Amount,Interest,Time,Choice,Period)
		v=f.clacu()
		if Choice == 1:
			mode="Annually"
		elif Choice ==2:
			mode="Half Yearly"
		elif Choice == 3:
			mode="Quarterly"
		elif Choice == 4:
			mode="Monthly"
		return render(request,"index.html", {'show':v,'rate_of_interest':Interest,"mode":mode})
	return render(request,"index.html")



