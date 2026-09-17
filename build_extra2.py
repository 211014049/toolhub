#!/usr/bin/env python3
"""Generate batch 2 of high-value tool pages for ToolHub."""
import os

OUT = os.path.join(os.path.dirname(__file__), "docs")
SITE_URL = "https://211014049.github.io/toolhub"

def make_page(filename, title, desc, category, keywords, html_body, js_code, related_tools):
    related_html = "".join(f'<a href="{r[0]}">{r[1]}</a>' for r in related_tools)
    category_slug = category.lower().replace(" ", "-").replace("&", "and").replace("/", "-")

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - Free Online Tool | ToolHub</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}/{filename}">
<link rel="canonical" href="{SITE_URL}/{filename}">
<link rel="stylesheet" href="/static/style.css">
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "{title}", "applicationCategory": "{category}", "operatingSystem": "Any (web browser)", "description": "{desc}", "offers": {{"@type": "Offer", "price": "0", "priceCurrency": "USD"}}, "url": "{SITE_URL}/{filename}"}}</script>
</head>
<body>
<header>
  <div class="header-inner">
    <a href="/" class="logo">Tool<span>Hub</span></a>
    <div class="search-bar">
      <input type="text" placeholder="Search tools..." id="search-input">
      <div class="search-results" id="search-results"></div>
    </div>
  </div>
</header>
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a> <span class="sep">&rsaquo;</span> <a href="/#category-{category_slug}">{category}</a> <span class="sep">&rsaquo;</span> {title}</div>
  <h1>{title}</h1>
  <p class="subtitle">{desc}</p>
  <div class="ad-slot"></div>
  <div class="tool-card">
{html_body}
  </div>
  <div class="info-section">
<h2>About {title}</h2>
<p>{desc}</p>
<p>This tool runs entirely in your browser. Your data is never sent to any server, ensuring complete privacy and security.</p>
  </div>
  <div class="related"><h2>Related Tools</h2><div class="related-grid">{related_html}</div></div>
  <div class="ad-slot"></div>
</div>
<footer>
  <p>ToolHub &mdash; Free Online Tools | <a href="/">All Tools</a></p>
  <p>&copy; 2026 ToolHub. All tools run in your browser. No data sent to servers.</p>
</footer>
<script src="/static/app.js"></script>
<script>{js_code}</script>
</body>
</html>"""

    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"  Created: {filename}")

TOOLS = []
REL = [("loan-calculator.html","Loan Calculator"),("mortgage-calculator.html","Mortgage Calculator"),("roi-calculator.html","ROI Calculator"),("percentage-calculator.html","Percentage Calculator")]

# ============================================================
# BUSINESS CALCULATORS
# ============================================================

TOOLS.append({
    "filename": "profit-margin-calculator.html",
    "title": "Profit Margin Calculator",
    "desc": "Calculate profit margin, gross margin and net margin from revenue and cost. Free online profit margin calculator.",
    "category": "Business Calculators",
    "keywords": "profit margin calculator, gross margin, net margin, profit percentage, business margin calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Revenue ($)</label><input type="number" id="revenue" value="100000" oninput="calcPM()"></div>
  <div class="input-group"><label>Cost ($)</label><input type="number" id="cost" value="60000" oninput="calcPM()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Profit Margin</div>
  <div class="value" id="margin">40%</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Profit: <strong id="profit">$40,000</strong></span>
    <span>Markup: <strong id="markup">66.67%</strong></span>
  </div>
</div>
""",
    "js": """
function calcPM(){const r=parseFloat(document.getElementById('revenue').value)||0;const c=parseFloat(document.getElementById('cost').value)||0;const p=r-c;const margin=r>0?(p/r*100):0;const markup=c>0?(p/c*100):0;document.getElementById('margin').textContent=margin.toFixed(2)+'%';document.getElementById('profit').textContent='$'+p.toLocaleString('en-US');document.getElementById('markup').textContent=markup.toFixed(2)+'%'}
calcPM();
"""
})

TOOLS.append({
    "filename": "markup-calculator.html",
    "title": "Markup Calculator",
    "desc": "Calculate markup percentage from cost and selling price. Free online markup calculator for retail and wholesale.",
    "category": "Business Calculators",
    "keywords": "markup calculator, markup percentage, retail markup, wholesale markup, price markup",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Cost ($)</label><input type="number" id="cost" value="50" oninput="calcMarkup()"></div>
  <div class="input-group"><label>Selling Price ($)</label><input type="number" id="price" value="75" oninput="calcMarkup()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Markup</div>
  <div class="value" id="markup">50%</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Profit: <strong id="profit">$25.00</strong></span>
    <span>Margin: <strong id="margin">33.33%</strong></span>
  </div>
</div>
""",
    "js": """
function calcMarkup(){const c=parseFloat(document.getElementById('cost').value)||0;const p=parseFloat(document.getElementById('price').value)||0;const profit=p-c;const markup=c>0?(profit/c*100):0;const margin=p>0?(profit/p*100):0;document.getElementById('markup').textContent=markup.toFixed(2)+'%';document.getElementById('profit').textContent='$'+profit.toFixed(2);document.getElementById('margin').textContent=margin.toFixed(2)+'%'}
calcMarkup();
"""
})

TOOLS.append({
    "filename": "break-even-calculator.html",
    "title": "Break-Even Calculator",
    "desc": "Calculate break-even point in units and dollars. Free online break-even analysis calculator for business planning.",
    "category": "Business Calculators",
    "keywords": "break-even calculator, break-even point, break-even analysis, bep calculator, break even sales",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Fixed Costs ($)</label><input type="number" id="fixed" value="10000" oninput="calcBE()"></div>
  <div class="input-group"><label>Price per Unit ($)</label><input type="number" id="price" value="25" step="0.01" oninput="calcBE()"></div>
  <div class="input-group"><label>Variable Cost per Unit ($)</label><input type="number" id="variable" value="10" step="0.01" oninput="calcBE()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Break-Even Point</div>
  <div class="value" id="units">667 units</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Break-Even Revenue: <strong id="revenue">$16,666.67</strong></span>
    <span>Contribution Margin: <strong id="cm">$15.00</strong></span>
  </div>
</div>
""",
    "js": """
function calcBE(){const f=parseFloat(document.getElementById('fixed').value)||0;const p=parseFloat(document.getElementById('price').value)||0;const v=parseFloat(document.getElementById('variable').value)||0;const cm=p-v;if(cm<=0){document.getElementById('units').textContent='Cannot break even';return}const units=Math.ceil(f/cm);document.getElementById('units').textContent=units.toLocaleString('en-US')+' units';document.getElementById('revenue').textContent='$'+(units*p).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});document.getElementById('cm').textContent='$'+cm.toFixed(2)}
calcBE();
"""
})

TOOLS.append({
    "filename": "savings-goal-calculator.html",
    "title": "Savings Goal Calculator",
    "desc": "Calculate how much to save monthly to reach your savings goal. Free online savings goal calculator.",
    "category": "Business Calculators",
    "keywords": "savings goal calculator, savings planner, how much to save, savings target, savings calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Savings Goal ($)</label><input type="number" id="goal" value="50000" oninput="calcSG()"></div>
  <div class="input-group"><label>Current Savings ($)</label><input type="number" id="current" value="5000" oninput="calcSG()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Months to Save</label><input type="number" id="months" value="24" oninput="calcSG()"></div>
  <div class="input-group"><label>Annual Interest (%)</label><input type="number" id="rate" value="4" step="0.1" oninput="calcSG()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Monthly Savings Needed</div>
  <div class="value" id="monthly">$1,854.37</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Total Contributions: <strong id="contrib">$44,444.44</strong> | Interest Earned: <strong id="interest">$555.56</strong></div>
</div>
""",
    "js": """
function calcSG(){const goal=parseFloat(document.getElementById('goal').value)||0;const curr=parseFloat(document.getElementById('current').value)||0;const n=parseInt(document.getElementById('months').value)||0;const r=(parseFloat(document.getElementById('rate').value)||0)/100/12;const need=goal-curr;if(n<=0||need<=0){document.getElementById('monthly').textContent='$0.00';return}let monthly;if(r===0){monthly=need/n}else{monthly=need*r/(Math.pow(1+r,n)-1)}const contrib=monthly*n;const interest=need-contrib;document.getElementById('monthly').textContent='$'+monthly.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});document.getElementById('contrib').textContent='$'+contrib.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});document.getElementById('interest').textContent='$'+Math.abs(interest).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}
calcSG();
"""
})

TOOLS.append({
    "filename": "credit-card-payoff-calculator.html",
    "title": "Credit Card Payoff Calculator",
    "desc": "Calculate how long it takes to pay off credit card debt and total interest paid. Free online credit card payoff calculator.",
    "category": "Business Calculators",
    "keywords": "credit card payoff calculator, debt payoff calculator, credit card debt, debt free calculator, payoff plan",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Balance ($)</label><input type="number" id="balance" value="5000" oninput="calcCC()"></div>
  <div class="input-group"><label>APR (%)</label><input type="number" id="apr" value="19.99" step="0.01" oninput="calcCC()"></div>
  <div class="input-group"><label>Monthly Payment ($)</label><input type="number" id="payment" value="200" oninput="calcCC()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Time to Pay Off</div>
  <div class="value" id="months">33 months</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Total Interest: <strong id="interest">$1,503.42</strong></span>
    <span>Total Paid: <strong id="total">$6,503.42</strong></span>
  </div>
</div>
""",
    "js": """
function calcCC(){let bal=parseFloat(document.getElementById('balance').value)||0;const apr=parseFloat(document.getElementById('apr').value)||0;const pay=parseFloat(document.getElementById('payment').value)||0;const r=apr/100/12;if(pay<=bal*r+1&&r>0){document.getElementById('months').textContent='Payment too low - will never pay off';return}let months=0;let interest=0;while(bal>0&&months<600){const i=bal*r;interest+=i;bal+=i-pay;if(bal<0)interest+=bal;months++}document.getElementById('months').textContent=months+' months ('+(months/12).toFixed(1)+' years)';document.getElementById('interest').textContent='$'+interest.toFixed(2);document.getElementById('total').textContent='$'+(interest+parseFloat(document.getElementById('balance').value)).toFixed(2)}
calcCC();
"""
})

TOOLS.append({
    "filename": "net-worth-calculator.html",
    "title": "Net Worth Calculator",
    "desc": "Calculate your net worth from total assets and liabilities. Free online net worth calculator.",
    "category": "Business Calculators",
    "keywords": "net worth calculator, assets minus liabilities, personal net worth, wealth calculator, net worth tracker",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Total Assets ($)</label><input type="number" id="assets" value="350000" oninput="calcNW()"></div>
  <div class="input-group"><label>Total Liabilities ($)</label><input type="number" id="liabilities" value="150000" oninput="calcNW()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Net Worth</div>
  <div class="value" id="networth">$200,000</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Debt-to-Asset Ratio: <strong id="ratio">42.86%</strong></div>
</div>
""",
    "js": """
function calcNW(){const a=parseFloat(document.getElementById('assets').value)||0;const l=parseFloat(document.getElementById('liabilities').value)||0;const nw=a-l;document.getElementById('networth').textContent=(nw<0?'-$':'$')+Math.abs(nw).toLocaleString('en-US');document.getElementById('ratio').textContent=a>0?(l/a*100).toFixed(2)+'%':'0%'}
calcNW();
"""
})

TOOLS.append({
    "filename": "inflation-calculator.html",
    "title": "Inflation Calculator",
    "desc": "Calculate how much money will be worth in the future due to inflation. Free online inflation calculator.",
    "category": "Business Calculators",
    "keywords": "inflation calculator, future value, inflation rate, purchasing power, money devaluation",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Current Amount ($)</label><input type="number" id="amount" value="10000" oninput="calcInf()"></div>
  <div class="input-group"><label>Inflation Rate (%)</label><input type="number" id="rate" value="3" step="0.1" oninput="calcInf()"></div>
  <div class="input-group"><label>Years</label><input type="number" id="years" value="10" oninput="calcInf()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Future Value Needed</div>
  <div class="value" id="future">$13,439.16</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Purchasing Power Loss: <strong id="loss">$3,439.16 (34.39%)</strong></div>
</div>
""",
    "js": """
function calcInf(){const a=parseFloat(document.getElementById('amount').value)||0;const r=parseFloat(document.getElementById('rate').value)||0;const y=parseInt(document.getElementById('years').value)||0;const future=a*Math.pow(1+r/100,y);const loss=future-a;document.getElementById('future').textContent='$'+future.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});document.getElementById('loss').textContent='$'+loss.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})+' ('+(loss/a*100).toFixed(2)+'%)'}
calcInf();
"""
})

TOOLS.append({
    "filename": "hourly-to-salary-calculator.html",
    "title": "Hourly to Salary Calculator",
    "desc": "Convert hourly wage to annual salary. Free online hourly to salary converter with overtime and tax estimates.",
    "category": "Business Calculators",
    "keywords": "hourly to salary, hourly wage to annual salary, wage converter, annual income calculator, hourly to yearly",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Hourly Rate ($)</label><input type="number" id="rate" value="25" step="0.01" oninput="calcHS()"></div>
  <div class="input-group"><label>Hours per Week</label><input type="number" id="hours" value="40" oninput="calcHS()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Annual Salary</div>
  <div class="value" id="annual">$52,000</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Monthly: <strong id="monthly">$4,333</strong></span>
    <span>Weekly: <strong id="weekly">$1,000</strong></span>
    <span>Daily: <strong id="daily">$200</strong></span>
  </div>
</div>
""",
    "js": """
function calcHS(){const r=parseFloat(document.getElementById('rate').value)||0;const h=parseFloat(document.getElementById('hours').value)||0;const weekly=r*h;const annual=weekly*52;document.getElementById('annual').textContent='$'+annual.toLocaleString('en-US');document.getElementById('monthly').textContent='$'+Math.round(annual/12).toLocaleString('en-US');document.getElementById('weekly').textContent='$'+weekly.toLocaleString('en-US');document.getElementById('daily').textContent='$'+(r*h/5).toLocaleString('en-US')}
calcHS();
"""
})

# ============================================================
# PROBABILITY & STATISTICS CALCULATORS
# ============================================================

TOOLS.append({
    "filename": "permutation-combination-calculator.html",
    "title": "Permutation and Combination Calculator",
    "desc": "Calculate permutations nPr and combinations nCr. Free online permutation and combination calculator.",
    "category": "Math Calculators",
    "keywords": "permutation calculator, combination calculator, npr, ncr, permutation and combination, probability calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>n (total items)</label><input type="number" id="n" value="10" oninput="calcPC()"></div>
  <div class="input-group"><label>r (chosen items)</label><input type="number" id="r" value="3" oninput="calcPC()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Results</div>
  <div style="margin-top:8px">
    <div style="padding:4px 0">Permutations (nPr): <strong id="npr">720</strong></div>
    <div style="padding:4px 0">Combinations (nCr): <strong id="ncr">120</strong></div>
  </div>
</div>
""",
    "js": """
function fact(n){if(n<2)return 1;let r=1;for(let i=2;i<=n;i++)r*=i;return r}
function calcPC(){const n=parseInt(document.getElementById('n').value)||0;const r=parseInt(document.getElementById('r').value)||0;if(n<0||r<0||r>n){document.getElementById('npr').textContent='Invalid';document.getElementById('ncr').textContent='Invalid';return}const p=fact(n)/fact(n-r);const c=fact(n)/(fact(r)*fact(n-r));document.getElementById('npr').textContent=p.toLocaleString('en-US');document.getElementById('ncr').textContent=c.toLocaleString('en-US')}
calcPC();
"""
})

TOOLS.append({
    "filename": "factorial-calculator.html",
    "title": "Factorial Calculator",
    "desc": "Calculate the factorial of any non-negative integer. Free online factorial calculator n!.",
    "category": "Math Calculators",
    "keywords": "factorial calculator, n factorial, factorial calculator online, calculate factorial, math factorial",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Number (n)</label><input type="number" id="n" value="10" min="0" oninput="calcFact()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">n!</div>
  <div class="value" id="result">3,628,800</div>
</div>
<div style="margin-top:8px;font-size:12px;color:var(--text-soft)">Supports n up to 170. Factorials of n>170 exceed JavaScript number precision.</div>
""",
    "js": """
function calcFact(){const n=parseInt(document.getElementById('n').value);if(isNaN(n)||n<0){document.getElementById('result').textContent='Enter a non-negative integer';return}if(n>170){document.getElementById('result').textContent='Infinity (too large)';return}let r=1;for(let i=2;i<=n;i++)r*=i;document.getElementById('result').textContent=r.toLocaleString('en-US',{maximumFractionDigits:0})}
calcFact();
"""
})

TOOLS.append({
    "filename": "prime-number-checker.html",
    "title": "Prime Number Checker",
    "desc": "Check if a number is prime and find prime factors. Free online prime number checker and tester.",
    "category": "Math Calculators",
    "keywords": "prime number checker, prime checker, is it prime, prime number test, prime factorization",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Number</label><input type="number" id="n" value="97" min="2" oninput="checkPrime()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Result</div>
  <div class="value" id="result">97 is a prime number</div>
</div>
<div id="factors-box" style="margin-top:12px;display:none">
  <div class="label">Prime Factors</div>
  <div id="factors" style="margin-top:4px"></div>
</div>
""",
    "js": """
function checkPrime(){const n=parseInt(document.getElementById('n').value);if(isNaN(n)||n<2){document.getElementById('result').textContent='Enter a number >= 2';document.getElementById('factors-box').style.display='none';return}let isPrime=true;if(n===2){isPrime=true}else if(n%2===0){isPrime=false}else{for(let i=3;i<=Math.sqrt(n);i+=2){if(n%i===0){isPrime=false;break}}}document.getElementById('result').textContent=n+' is '+(isPrime?'a prime number':'not a prime number');if(!isPrime){const factors=[];let x=n;for(let i=2;i<=x;i++){while(x%i===0){factors.push(i);x/=i}}document.getElementById('factors').textContent=n+' = '+factors.join(' x ');document.getElementById('factors-box').style.display='block'}else{document.getElementById('factors-box').style.display='none'}}
checkPrime();
"""
})

TOOLS.append({
    "filename": "random-number-generator.html",
    "title": "Random Number Generator",
    "desc": "Generate random numbers within a range. Free online random number generator and dice roller.",
    "category": "Math Calculators",
    "keywords": "random number generator, rng, random number, random picker, number generator online",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Minimum</label><input type="number" id="min" value="1" oninput="gen()"></div>
  <div class="input-group"><label>Maximum</label><input type="number" id="max" value="100" oninput="gen()"></div>
  <div class="input-group"><label>Count</label><input type="number" id="count" value="1" min="1" max="100" oninput="gen()"></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="gen()">Generate</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Random Numbers</div>
  <div class="value" id="result" style="word-break:break-all">42</div>
</div>
<div style="margin-top:8px"><label style="font-size:14px;font-weight:normal"><input type="checkbox" id="unique" onchange="gen()"> Allow duplicates</label></div>
""",
    "js": """
function gen(){const min=parseInt(document.getElementById('min').value)||0;const max=parseInt(document.getElementById('max').value)||0;const count=parseInt(document.getElementById('count').value)||1;const uniq=!document.getElementById('unique').checked;if(min>max){document.getElementById('result').textContent='Min must be <= Max';return}if(uniq&&count>(max-min+1)){document.getElementById('result').textContent='Range too small for unique numbers';return}const nums=[];const pool=[];if(uniq){for(let i=min;i<=max;i++)pool.push(i);for(let i=0;i<count;i++){const idx=Math.floor(Math.random()*pool.length);nums.push(pool.splice(idx,1)[0])}}else{for(let i=0;i<count;i++)nums.push(Math.floor(Math.random()*(max-min+1))+min)}document.getElementById('result').textContent=nums.join(', ')}
gen();
"""
})

TOOLS.append({
    "filename": "standard-deviation-calculator.html",
    "title": "Standard Deviation Calculator",
    "desc": "Calculate standard deviation, variance, mean and range of a data set. Free online statistics calculator.",
    "category": "Math Calculators",
    "keywords": "standard deviation calculator, variance calculator, statistics calculator, mean calculator, sd calculator",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Data (comma separated)</label><input type="text" id="data" value="2, 4, 4, 4, 5, 5, 7, 9" oninput="calcSD()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Statistics</div>
  <div style="margin-top:8px">
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Mean</span><strong id="mean">5</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Standard Deviation</span><strong id="sd">2</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Variance</span><strong id="var">4</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Min / Max</span><strong id="minmax">2 / 9</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Count</span><strong id="count">8</strong></div>
  </div>
</div>
""",
    "js": """
function calcSD(){const nums=document.getElementById('data').value.split(',').map(s=>parseFloat(s.trim())).filter(n=>!isNaN(n));if(nums.length<2){document.getElementById('mean').textContent='Need 2+ numbers';return}const n=nums.length;const mean=nums.reduce((a,b)=>a+b,0)/n;const variance=nums.reduce((a,b)=>a+(b-mean)**2,0)/n;const sd=Math.sqrt(variance);document.getElementById('mean').textContent=mean.toFixed(4);document.getElementById('sd').textContent=sd.toFixed(4);document.getElementById('var').textContent=variance.toFixed(4);document.getElementById('minmax').textContent=Math.min(...nums)+' / '+Math.max(...nums);document.getElementById('count').textContent=n}
calcSD();
"""
})

# ============================================================
# MORE DEVELOPER TOOLS
# ============================================================

TOOLS.append({
    "filename": "timestamp-converter.html",
    "title": "Unix Timestamp Converter",
    "desc": "Convert Unix timestamps to human-readable dates and vice versa. Free online epoch timestamp converter.",
    "category": "Developer Tools",
    "keywords": "unix timestamp converter, epoch converter, timestamp to date, date to timestamp, unix time converter",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Unix Timestamp</label><input type="number" id="ts" oninput="tsToDate()" style="font-family:'Courier New',monospace"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Date (UTC)</div>
  <div class="value" id="dateutc" style="font-size:16px"></div>
  <div style="margin-top:4px;font-size:14px;color:var(--text-soft)">Local: <strong id="datelocal"></strong></div>
</div>
<div style="margin-top:16px;border-top:1px solid var(--border);padding-top:16px">
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Date</label><input type="datetime-local" id="dt" oninput="dateToTs()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Unix Timestamp</div>
  <div class="value" id="tsout" style="font-family:'Courier New',monospace"></div>
</div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="setNow()">Use Current Time</button></div>
""",
    "js": """
function tsToDate(){const ts=parseInt(document.getElementById('ts').value);if(isNaN(ts))return;const d=new Date(ts*1000);document.getElementById('dateutc').textContent=d.toUTCString();document.getElementById('datelocal').textContent=d.toLocaleString()}
function dateToTs(){const v=document.getElementById('dt').value;if(!v)return;const d=new Date(v);document.getElementById('tsout').textContent=Math.floor(d.getTime()/1000)}
function setNow(){const now=Math.floor(Date.now()/1000);document.getElementById('ts').value=now;tsToDate();const d=new Date();const off=d.getTimezoneOffset()*60000;document.getElementById('dt').value=new Date(d.getTime()-off).toISOString().slice(0,16);dateToTs()}
setNow();
"""
})

TOOLS.append({
    "filename": "html-formatter.html",
    "title": "HTML Formatter",
    "desc": "Format and beautify HTML code with proper indentation. Free online HTML formatter and beautifier.",
    "category": "Developer Tools",
    "keywords": "html formatter, html beautifier, format html, html indent, pretty print html",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>HTML Input</label><textarea id="input" placeholder="<html><body><h1>Hello</h1></body></html>" style="min-height:120px"><div><p>Hello</p><p>World</p></div></textarea></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="formatHTML()">Format</button><button class="btn btn-secondary" onclick="copyResult()">Copy</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Formatted HTML</div>
  <textarea id="output" style="margin-top:8px" readonly></textarea>
</div>
""",
    "js": """
function formatHTML(){let html=document.getElementById('input').value;let indent=0;let result='';const tokens=html.replace(/></g,'>\\n<').split('\\n');for(let line of tokens){line=line.trim();if(!line)continue;if(line.startsWith('</'))indent--;result+='  '.repeat(Math.max(0,indent))+line+'\\n';if(line.startsWith('<')&&!line.startsWith('</')&&!line.startsWith('<img')&&!line.startsWith('<br')&&!line.startsWith('<input')&&!line.startsWith('<meta')&&!line.startsWith('<hr')&&!line.startsWith('<link')&&!line.endsWith('/>')){if(!line.includes('</')||line.lastIndexOf('<')<line.lastIndexOf('</'))indent++}}document.getElementById('output').value=result.trim()}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').value)}
formatHTML();
"""
})

TOOLS.append({
    "filename": "xml-formatter.html",
    "title": "XML Formatter",
    "desc": "Format and beautify XML code with proper indentation. Free online XML formatter and beautifier.",
    "category": "Developer Tools",
    "keywords": "xml formatter, xml beautifier, format xml, xml indent, pretty print xml",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>XML Input</label><textarea id="input" placeholder="<root><item>value</item></root>" style="min-height:120px"><root><item>value</item><item>value2</item></root></textarea></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="formatXML()">Format</button><button class="btn btn-secondary" onclick="copyResult()">Copy</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Formatted XML</div>
  <textarea id="output" style="margin-top:8px" readonly></textarea>
</div>
""",
    "js": """
function formatXML(){let xml=document.getElementById('input').value;let indent=0;let result='';const tokens=xml.replace(/></g,'>\\n<').split('\\n');for(let line of tokens){line=line.trim();if(!line)continue;if(line.startsWith('</'))indent--;result+='  '.repeat(Math.max(0,indent))+line+'\\n';if(line.startsWith('<')&&!line.startsWith('</')&&!line.endsWith('/>')){if(!line.includes('</')||line.lastIndexOf('<')<line.lastIndexOf('</'))indent++}}document.getElementById('output').value=result.trim()}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').value)}
formatXML();
"""
})

TOOLS.append({
    "filename": "css-box-shadow-generator.html",
    "title": "CSS Box Shadow Generator",
    "desc": "Generate CSS box-shadow code with live preview. Free online CSS box shadow generator.",
    "category": "Developer Tools",
    "keywords": "css box shadow generator, box shadow, css shadow, shadow generator, box shadow code",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>X Offset (px)</label><input type="number" id="x" value="5" oninput="gen()"></div>
  <div class="input-group"><label>Y Offset (px)</label><input type="number" id="y" value="5" oninput="gen()"></div>
  <div class="input-group"><label>Blur (px)</label><input type="number" id="blur" value="10" oninput="gen()"></div>
  <div class="input-group"><label>Spread (px)</label><input type="number" id="spread" value="0" oninput="gen()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Color</label><input type="color" id="color" value="#000000" oninput="gen()"></div>
  <div class="input-group"><label>Opacity</label><input type="range" id="opacity" value="0.3" min="0" max="1" step="0.05" oninput="gen()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Preview</div>
  <div style="margin-top:12px;padding:40px;background:#f5f5f5;border-radius:8px">
    <div id="preview" style="width:120px;height:80px;background:#3366ff;border-radius:8px;margin:0 auto"></div>
  </div>
  <div style="margin-top:12px">
    <code id="code" style="display:block;padding:12px;background:var(--card);border-radius:6px;font-family:'Courier New',monospace;font-size:13px;word-break:break-all">box-shadow: 5px 5px 10px 0px rgba(0,0,0,0.3);</code>
  </div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="copyCode()">Copy CSS</button></div>
""",
    "js": """
function gen(){const x=document.getElementById('x').value;const y=document.getElementById('y').value;const b=document.getElementById('blur').value;const s=document.getElementById('spread').value;const c=document.getElementById('color').value;const o=document.getElementById('opacity').value;const r=parseInt(c.substr(1,2),16);const g=parseInt(c.substr(3,2),16);const bl=parseInt(c.substr(5,2),16);const shadow=x+'px '+y+'px '+b+'px '+s+'px rgba('+r+','+g+','+bl+','+o+')';document.getElementById('preview').style.boxShadow=shadow;document.getElementById('code').textContent='box-shadow: '+shadow+';'}
function copyCode(){navigator.clipboard.writeText(document.getElementById('code').textContent)}
gen();
"""
})

TOOLS.append({
    "filename": "ascii-table.html",
    "title": "ASCII Character Table",
    "desc": "Browse the complete ASCII character table with decimal, hex and binary values. Free online ASCII reference.",
    "category": "Developer Tools",
    "keywords": "ascii table, ascii characters, ascii codes, ascii reference, character encoding table",
    "html": """
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">ASCII Table (32-126)</div>
  <div id="table" style="margin-top:8px"></div>
</div>
""",
    "js": """
function buildTable(){let html='<table style="width:100%;border-collapse:collapse;font-size:13px"><tr style="border-bottom:2px solid var(--border)"><th style="padding:4px 8px;text-align:left">Char</th><th style="padding:4px 8px;text-align:left">Dec</th><th style="padding:4px 8px;text-align:left">Hex</th><th style="padding:4px 8px;text-align:left">Binary</th><th style="padding:4px 8px;text-align:left">Description</th></tr>';const names={32:'Space',33:'Exclamation',34:'Quotation',35:'Hash',36:'Dollar',37:'Percent',38:'Ampersand',39:'Apostrophe',40:'Left Paren',41:'Right Paren',42:'Asterisk',43:'Plus',44:'Comma',45:'Hyphen',46:'Period',47:'Slash',58:'Colon',59:'Semicolon',60:'Less Than',61:'Equals',62:'Greater Than',63:'Question',64:'At',91:'Left Bracket',92:'Backslash',93:'Right Bracket',94:'Caret',95:'Underscore',96:'Backtick',123:'Left Brace',124:'Pipe',125:'Right Brace',126:'Tilde'};for(let i=32;i<=126;i++){const ch=i===32?'&nbsp;':String.fromCharCode(i);const hex=i.toString(16).toUpperCase();const bin=i.toString(2).padStart(8,'0');const name=names[i]||String.fromCharCode(i);html+='<tr style="border-bottom:1px solid var(--border)"><td style="padding:4px 8px;font-family:Courier New">'+ch+'</td><td style="padding:4px 8px">'+i+'</td><td style="padding:4px 8px">0x'+hex+'</td><td style="padding:4px 8px">'+bin+'</td><td style="padding:4px 8px">'+name+'</td></tr>'}html+='</table>';document.getElementById('table').innerHTML=html}
buildTable();
"""
})

TOOLS.append({
    "filename": "html-to-markdown.html",
    "title": "HTML to Markdown Converter",
    "desc": "Convert HTML code to Markdown format. Free online HTML to Markdown converter.",
    "category": "Developer Tools",
    "keywords": "html to markdown, html to md, convert html to markdown, html markdown converter, html to md converter",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>HTML Input</label><textarea id="input" placeholder="<h1>Title</h1><p>Paragraph</p>" style="min-height:120px"><h1>Hello World</h1>
<p>This is <strong>bold</strong> and <em>italic</em>.</p>
<ul><li>Item 1</li><li>Item 2</li></ul></textarea></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="convert()">Convert</button><button class="btn btn-secondary" onclick="copyResult()">Copy</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Markdown Output</div>
  <textarea id="output" style="margin-top:8px" readonly></textarea>
</div>
""",
    "js": """
function convert(){let h=document.getElementById('input').value;h=h.replace(/<h1[^>]*>(.*?)<\\/h1>/gi,'## $1\\n');h=h.replace(/<h2[^>]*>(.*?)<\\/h2>/gi,'## $1\\n');h=h.replace(/<h3[^>]*>(.*?)<\\/h3>/gi,'### $1\\n');h=h.replace(/<h4[^>]*>(.*?)<\\/h4>/gi,'#### $1\\n');h=h.replace(/<strong[^>]*>(.*?)<\\/strong>/gi,'**$1**');h=h.replace(/<b[^>]*>(.*?)<\\/b>/gi,'**$1**');h=h.replace(/<em[^>]*>(.*?)<\\/em>/gi,'*$1*');h=h.replace(/<i[^>]*>(.*?)<\\/i>/gi,'*$1*');h=h.replace(/<a[^>]*href="(.*?)"[^>]*>(.*?)<\\/a>/gi,'[$2]($1)');h=h.replace(/<li[^>]*>(.*?)<\\/li>/gi,'- $1\\n');h=h.replace(/<ul[^>]*>/gi,'\\n');h=h.replace(/<\\/ul>/gi,'\\n');h=h.replace(/<p[^>]*>(.*?)<\\/p>/gi,'$1\\n\\n');h=h.replace(/<br\\s*\\/?>/gi,'\\n');h=h.replace(/<[^>]+>/g,'');h=h.replace(/\\n{3,}/g,'\\n\\n');document.getElementById('output').value=h.trim()}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').value)}
convert();
"""
})

# ============================================================
# MORE TEXT TOOLS
# ============================================================

TOOLS.append({
    "filename": "text-diff-checker.html",
    "title": "Text Diff Checker",
    "desc": "Compare two texts and highlight differences. Free online text comparison and diff tool.",
    "category": "Text Tools",
    "keywords": "text diff checker, text comparison, compare text, text difference, diff tool online",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Original Text</label><textarea id="text1" placeholder="Enter original text..." style="min-height:100px">The quick brown fox
jumps over the lazy dog
Hello World</textarea></div>
</div>
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Modified Text</label><textarea id="text2" placeholder="Enter modified text..." style="min-height:100px">The quick brown fox
jumps over the lazy cat
Hello World
New line</textarea></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="compareText()">Compare</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Differences</div>
  <div id="output" style="margin-top:8px;font-family:'Courier New',monospace;font-size:13px"></div>
</div>
""",
    "js": """
function compareText(){const l1=document.getElementById('text1').value.split('\\n');const l2=document.getElementById('text2').value.split('\\n');const max=Math.max(l1.length,l2.length);let html='';for(let i=0;i<max;i++){const a=l1[i]||'';const b=l2[i]||'';if(a===b){html+='<div style="padding:2px 0;color:var(--text-soft)">  '+escapeHTML(a)+'</div>'}else{if(a)html+='<div style="padding:2px 0;color:#c62828;background:rgba(198,40,40,0.05)">- '+escapeHTML(a)+'</div>';if(b)html+='<div style="padding:2px 0;color:#2e7d32;background:rgba(46,125,50,0.05)">+ '+escapeHTML(b)+'</div>'}}document.getElementById('output').innerHTML=html}
function escapeHTML(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
compareText();
"""
})

TOOLS.append({
    "filename": "reading-time-calculator.html",
    "title": "Reading Time Calculator",
    "desc": "Calculate estimated reading time for text. Free online reading time and word count estimator.",
    "category": "Text Tools",
    "keywords": "reading time calculator, reading time estimator, words per minute, read time, article reading time",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Text</label><textarea id="input" placeholder="Paste your text here..." oninput="calcRT()">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</textarea></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Reading Speed (wpm)</label><input type="number" id="wpm" value="200" oninput="calcRT()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Reading Time</div>
  <div class="value" id="time">0 min 22 sec</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Words: <strong id="words">44</strong></span>
    <span>Characters: <strong id="chars">230</strong></span>
    <span>Sentences: <strong id="sentences">3</strong></span>
  </div>
</div>
""",
    "js": """
function calcRT(){const t=document.getElementById('input').value;const wpm=parseInt(document.getElementById('wpm').value)||200;const words=(t.match(/\\b\\w+\\b/g)||[]).length;const chars=t.length;const sentences=(t.match(/[.!?]+/g)||[]).length;const sec=Math.ceil(words/wpm*60);const m=Math.floor(sec/60);const s=sec%60;document.getElementById('time').textContent=m+' min '+s+' sec';document.getElementById('words').textContent=words;document.getElementById('chars').textContent=chars;document.getElementById('sentences').textContent=sentences}
calcRT();
"""
})

TOOLS.append({
    "filename": "text-case-converter.html",
    "title": "Text Case Converter",
    "desc": "Convert text to camelCase, snake_case, kebab-case, CONSTANT_CASE and more. Free online text case converter.",
    "category": "Text Tools",
    "keywords": "text case converter, camel case, snake case, kebab case, constant case, text transform",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Input Text</label><textarea id="input" placeholder="Enter text..." oninput="convert()">Hello World This Is A Test</textarea></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Conversions</div>
  <div style="margin-top:8px">
    <div style="padding:4px 0;border-bottom:1px solid var(--border)">camelCase: <strong id="camel">helloWorldThisIsATest</strong></div>
    <div style="padding:4px 0;border-bottom:1px solid var(--border)">PascalCase: <strong id="pascal">HelloWorldThisIsATest</strong></div>
    <div style="padding:4px 0;border-bottom:1px solid var(--border)">snake_case: <strong id="snake">hello_world_this_is_a_test</strong></div>
    <div style="padding:4px 0;border-bottom:1px solid var(--border)">kebab-case: <strong id="kebab">hello-world-this-is-a-test</strong></div>
    <div style="padding:4px 0;border-bottom:1px solid var(--border)">CONSTANT_CASE: <strong id="constant">HELLO_WORLD_THIS_IS_A_TEST</strong></div>
    <div style="padding:4px 0">Title Case: <strong id="title">Hello World This Is A Test</strong></div>
  </div>
</div>
""",
    "js": """
function convert(){const t=document.getElementById('input').value;const words=t.match(/[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)|\\d+/g)||[];const lower=words.map(w=>w.toLowerCase());document.getElementById('camel').textContent=lower.map((w,i)=>i===0?w:w[0].toUpperCase()+w.slice(1)).join('');document.getElementById('pascal').textContent=lower.map(w=>w[0].toUpperCase()+w.slice(1)).join('');document.getElementById('snake').textContent=lower.join('_');document.getElementById('kebab').textContent=lower.join('-');document.getElementById('constant').textContent=lower.map(w=>w.toUpperCase()).join('_');document.getElementById('title').textContent=lower.map(w=>w[0].toUpperCase()+w.slice(1)).join(' ')}
convert();
"""
})

TOOLS.append({
    "filename": "line-number-adder.html",
    "title": "Line Number Adder",
    "desc": "Add line numbers to text. Free online text line number adder tool.",
    "category": "Text Tools",
    "keywords": "line number adder, add line numbers, number lines, text line counter, line numbering tool",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Text</label><textarea id="input" placeholder="Enter text..." oninput="addNumbers()">First line
Second line
Third line</textarea></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">With Line Numbers</div>
  <textarea id="output" style="margin-top:8px" readonly></textarea>
</div>
""",
    "js": """
function addNumbers(){const lines=document.getElementById('input').value.split('\\n');const padded=lines.map((l,i)=>(String(i+1).padStart(4,' '))+'| '+l);document.getElementById('output').value=padded.join('\\n')}
addNumbers();
"""
})

TOOLS.append({
    "filename": "text-trimmer.html",
    "title": "Text Trimmer",
    "desc": "Trim whitespace, remove extra spaces and clean up text. Free online text trimmer and cleaner.",
    "category": "Text Tools",
    "keywords": "text trimmer, trim whitespace, remove extra spaces, clean text, text cleaner",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Text</label><textarea id="input" placeholder="  Enter   messy   text...  " oninput="trimText()">  Hello   World   This   is   messy  </textarea></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn" onclick="trimText()">Trim</button>
  <button class="btn btn-secondary" onclick="squeezeSpaces()">Squeeze Spaces</button>
  <button class="btn btn-secondary" onclick="removeEmpty()">Remove Empty Lines</button>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Result</div>
  <textarea id="output" style="margin-top:8px" readonly></textarea>
</div>
""",
    "js": """
function trimText(){const t=document.getElementById('input').value;document.getElementById('output').value=t.split('\\n').map(l=>l.trim()).join('\\n').trim()}
function squeezeSpaces(){document.getElementById('output').value=document.getElementById('input').value.replace(/ +/g,' ').split('\\n').map(l=>l.trim()).join('\\n').trim()}
function removeEmpty(){document.getElementById('output').value=document.getElementById('input').value.split('\\n').filter(l=>l.trim()!=='').join('\\n')}
trimText();
"""
})

# ============================================================
# MORE UNIT CONVERTERS
# ============================================================

TOOLS.append({
    "filename": "fuel-economy-converter.html",
    "title": "Fuel Economy Converter",
    "desc": "Convert between MPG, L/100km, km/L and other fuel economy units. Free online fuel economy converter.",
    "category": "Calculators",
    "keywords": "fuel economy converter, mpg to l/100km, l/100km to mpg, fuel consumption converter, km/l to mpg",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Value</label><input type="number" id="value" value="30" step="0.1" oninput="convert()"></div>
  <div class="input-group"><label>From</label>
    <select id="from" onchange="convert()">
      <option value="mpg_us">MPG (US)</option>
      <option value="mpg_uk">MPG (UK)</option>
      <option value="l100km">L/100km</option>
      <option value="kml">km/L</option>
    </select>
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Converted Values</div>
  <div style="margin-top:8px">
    <div style="padding:4px 0">MPG (US): <strong id="mpg_us">30.00</strong></div>
    <div style="padding:4px 0">MPG (UK): <strong id="mpg_uk">36.02</strong></div>
    <div style="padding:4px 0">L/100km: <strong id="l100km">7.84</strong></div>
    <div style="padding:4px 0">km/L: <strong id="kml">12.75</strong></div>
  </div>
</div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('value').value)||0;const f=document.getElementById('from').value;let l100km;if(f==='mpg_us')l100km=235.215/v;else if(f==='mpg_uk')l100km=282.481/v;else if(f==='l100km')l100km=v;else l100km=100/v;document.getElementById('mpg_us').textContent=(235.215/l100km).toFixed(2);document.getElementById('mpg_uk').textContent=(282.481/l100km).toFixed(2);document.getElementById('l100km').textContent=l100km.toFixed(2);document.getElementById('kml').textContent=(100/l100km).toFixed(2)}
convert();
"""
})

TOOLS.append({
    "filename": "angle-converter.html",
    "title": "Angle Converter",
    "desc": "Convert between degrees, radians, gradians and turns. Free online angle converter.",
    "category": "Calculators",
    "keywords": "angle converter, degrees to radians, radians to degrees, gradian, angle conversion",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Degrees</label><input type="number" id="deg" value="90" step="any" oninput="fromDeg()"></div>
  <div class="input-group"><label>Radians</label><input type="number" id="rad" value="1.5708" step="any" oninput="fromRad()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Gradians</label><input type="number" id="grad" value="100" step="any" oninput="fromGrad()"></div>
  <div class="input-group"><label>Turns</label><input type="number" id="turn" value="0.25" step="any" oninput="fromTurn()"></div>
</div>
""",
    "js": """
function fromDeg(){const d=parseFloat(document.getElementById('deg').value)||0;document.getElementById('rad').value=(d*Math.PI/180).toFixed(6);document.getElementById('grad').value=(d*10/9).toFixed(6);document.getElementById('turn').value=(d/360).toFixed(6)}
function fromRad(){const r=parseFloat(document.getElementById('rad').value)||0;const d=r*180/Math.PI;document.getElementById('deg').value=d.toFixed(6);document.getElementById('grad').value=(d*10/9).toFixed(6);document.getElementById('turn').value=(d/360).toFixed(6)}
function fromGrad(){const g=parseFloat(document.getElementById('grad').value)||0;const d=g*0.9;document.getElementById('deg').value=d.toFixed(6);document.getElementById('rad').value=(d*Math.PI/180).toFixed(6);document.getElementById('turn').value=(d/360).toFixed(6)}
function fromTurn(){const t=parseFloat(document.getElementById('turn').value)||0;const d=t*360;document.getElementById('deg').value=d.toFixed(6);document.getElementById('rad').value=(d*Math.PI/180).toFixed(6);document.getElementById('grad').value=(d*10/9).toFixed(6)}
fromDeg();
"""
})

TOOLS.append({
    "filename": "power-converter.html",
    "title": "Power Converter",
    "desc": "Convert between watts, kilowatts, horsepower, BTU/hour and more. Free online power unit converter.",
    "category": "Calculators",
    "keywords": "power converter, watts to kilowatts, horsepower to watts, btu to watts, power unit converter",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Value</label><input type="number" id="value" value="1" step="any" oninput="convert()"></div>
  <div class="input-group"><label>From</label>
    <select id="from" onchange="convert()">
      <option value="w">Watt (W)</option>
      <option value="kw">Kilowatt (kW)</option>
      <option value="hp">Horsepower (hp)</option>
      <option value="btu">BTU/hour</option>
      <option value="mw">Megawatt (MW)</option>
    </select>
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Converted Values</div>
  <div style="margin-top:8px">
    <div style="padding:4px 0">Watts: <strong id="w">1.00</strong></div>
    <div style="padding:4px 0">Kilowatts: <strong id="kw">0.001</strong></div>
    <div style="padding:4px 0">Horsepower: <strong id="hp">0.0013</strong></div>
    <div style="padding:4px 0">BTU/hour: <strong id="btu">3.41</strong></div>
    <div style="padding:4px 0">Megawatts: <strong id="mw">0.000001</strong></div>
  </div>
</div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('value').value)||0;const f=document.getElementById('from').value;let w;if(f==='w')w=v;else if(f==='kw')w=v*1000;else if(f==='hp')w=v*745.7;else if(f==='btu')w=v/3.41214;else w=v*1000000;document.getElementById('w').textContent=w.toFixed(4);document.getElementById('kw').textContent=(w/1000).toFixed(6);document.getElementById('hp').textContent=(w/745.7).toFixed(6);document.getElementById('btu').textContent=(w*3.41214).toFixed(4);document.getElementById('mw').textContent=(w/1000000).toFixed(8)}
convert();
"""
})

TOOLS.append({
    "filename": "frequency-converter.html",
    "title": "Frequency Converter",
    "desc": "Convert between Hz, kHz, MHz, GHz and more. Free online frequency unit converter.",
    "category": "Calculators",
    "keywords": "frequency converter, hz to khz, mhz to ghz, frequency unit converter, hertz converter",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Value</label><input type="number" id="value" value="1" step="any" oninput="convert()"></div>
  <div class="input-group"><label>From</label>
    <select id="from" onchange="convert()">
      <option value="hz">Hertz (Hz)</option>
      <option value="khz">Kilohertz (kHz)</option>
      <option value="mhz">Megahertz (MHz)</option>
      <option value="ghz">Gigahertz (GHz)</option>
      <option value="rpm">RPM</option>
    </select>
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Converted Values</div>
  <div style="margin-top:8px">
    <div style="padding:4px 0">Hz: <strong id="hz">1.00</strong></div>
    <div style="padding:4px 0">kHz: <strong id="khz">0.001</strong></div>
    <div style="padding:4px 0">MHz: <strong id="mhz">0.000001</strong></div>
    <div style="padding:4px 0">GHz: <strong id="ghz">0.000000001</strong></div>
    <div style="padding:4px 0">RPM: <strong id="rpm">60.00</strong></div>
  </div>
</div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('value').value)||0;const f=document.getElementById('from').value;let hz;if(f==='hz')hz=v;else if(f==='khz')hz=v*1000;else if(f==='mhz')hz=v*1000000;else if(f==='ghz')hz=v*1000000000;else hz=v/60;document.getElementById('hz').textContent=hz.toFixed(4);document.getElementById('khz').textContent=(hz/1000).toFixed(8);document.getElementById('mhz').textContent=(hz/1000000).toFixed(12);document.getElementById('ghz').textContent=(hz/1000000000).toExponential(6);document.getElementById('rpm').textContent=(hz*60).toFixed(4)}
convert();
"""
})

# ============================================================
# MORE CONVERTERS
# ============================================================

TOOLS.append({
    "filename": "cooking-converter.html",
    "title": "Cooking Measurement Converter",
    "desc": "Convert cooking measurements: cups, tablespoons, teaspoons, ml, grams and more. Free online cooking converter.",
    "category": "Calculators",
    "keywords": "cooking converter, cup to tablespoon, teaspoon to ml, cooking measurement, recipe converter",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Value</label><input type="number" id="value" value="1" step="any" oninput="convert()"></div>
  <div class="input-group"><label>From</label>
    <select id="from" onchange="convert()">
      <option value="cup">Cup (US)</option>
      <option value="tbsp">Tablespoon</option>
      <option value="tsp">Teaspoon</option>
      <option value="ml">Milliliter</option>
      <option value="floz">Fluid Ounce</option>
      <option value="pint">Pint</option>
      <option value="quart">Quart</option>
    </select>
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Converted Values</div>
  <div style="margin-top:8px">
    <div style="padding:4px 0">Cups: <strong id="cup">1.00</strong></div>
    <div style="padding:4px 0">Tablespoons: <strong id="tbsp">16.00</strong></div>
    <div style="padding:4px 0">Teaspoons: <strong id="tsp">48.00</strong></div>
    <div style="padding:4px 0">Milliliters: <strong id="ml">236.59</strong></div>
    <div style="padding:4px 0">Fluid Ounces: <strong id="floz">8.00</strong></div>
  </div>
</div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('value').value)||0;const f=document.getElementById('from').value;const toMl={cup:236.588,tbsp:14.787,tsp:4.929,ml:1,floz:29.574,pint:473.176,quart:946.353};const ml=v*toMl[f];document.getElementById('cup').textContent=(ml/toMl.cup).toFixed(4);document.getElementById('tbsp').textContent=(ml/toMl.tbsp).toFixed(4);document.getElementById('tsp').textContent=(ml/toMl.tsp).toFixed(4);document.getElementById('ml').textContent=ml.toFixed(2);document.getElementById('floz').textContent=(ml/toMl.floz).toFixed(4)}
convert();
"""
})

TOOLS.append({
    "filename": "data-transfer-rate-converter.html",
    "title": "Data Transfer Rate Converter",
    "desc": "Convert between Mbps, Kbps, Gbps, MB/s and more. Free online data transfer rate converter.",
    "category": "Calculators",
    "keywords": "data transfer rate converter, mbps to mb/s, gbps to mbps, bandwidth converter, internet speed converter",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Value</label><input type="number" id="value" value="100" step="any" oninput="convert()"></div>
  <div class="input-group"><label>From</label>
    <select id="from" onchange="convert()">
      <option value="bps">bps</option>
      <option value="kbps">Kbps</option>
      <option value="mbps" selected>Mbps</option>
      <option value="gbps">Gbps</option>
      <option value="mbs">MB/s</option>
      <option value="gbs">GB/s</option>
    </select>
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Converted Values</div>
  <div style="margin-top:8px">
    <div style="padding:4px 0">bps: <strong id="bps">100,000,000</strong></div>
    <div style="padding:4px 0">Kbps: <strong id="kbps">100,000</strong></div>
    <div style="padding:4px 0">Mbps: <strong id="mbps">100.00</strong></div>
    <div style="padding:4px 0">Gbps: <strong id="gbps">0.10</strong></div>
    <div style="padding:4px 0">MB/s: <strong id="mbs">12.50</strong></div>
    <div style="padding:4px 0">GB/s: <strong id="gbs">0.01</strong></div>
  </div>
</div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('value').value)||0;const f=document.getElementById('from').value;let bps;if(f==='bps')bps=v;else if(f==='kbps')bps=v*1000;else if(f==='mbps')bps=v*1000000;else if(f==='gbps')bps=v*1000000000;else if(f==='mbs')bps=v*8000000;else bps=v*8000000000;document.getElementById('bps').textContent=bps.toLocaleString('en-US');document.getElementById('kbps').textContent=(bps/1000).toLocaleString('en-US');document.getElementById('mbps').textContent=(bps/1000000).toFixed(2);document.getElementById('gbps').textContent=(bps/1000000000).toFixed(4);document.getElementById('mbs').textContent=(bps/8000000).toFixed(4);document.getElementById('gbs').textContent=(bps/8000000000).toFixed(6)}
convert();
"""
})

TOOLS.append({
    "filename": "density-converter.html",
    "title": "Density Converter",
    "desc": "Convert between kg/m3, g/cm3, lb/ft3 and more density units. Free online density converter.",
    "category": "Calculators",
    "keywords": "density converter, kg/m3 to g/cm3, lb/ft3 to kg/m3, density unit converter, specific gravity",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Value</label><input type="number" id="value" value="1000" step="any" oninput="convert()"></div>
  <div class="input-group"><label>From</label>
    <select id="from" onchange="convert()">
      <option value="kgm3">kg/m3</option>
      <option value="gcm3">g/cm3</option>
      <option value="lbft3">lb/ft3</option>
      <option value="lbin3">lb/in3</option>
    </select>
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Converted Values</div>
  <div style="margin-top:8px">
    <div style="padding:4px 0">kg/m3: <strong id="kgm3">1000.00</strong></div>
    <div style="padding:4px 0">g/cm3: <strong id="gcm3">1.00</strong></div>
    <div style="padding:4px 0">lb/ft3: <strong id="lbft3">62.43</strong></div>
    <div style="padding:4px 0">lb/in3: <strong id="lbin3">0.036</strong></div>
  </div>
</div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('value').value)||0;const f=document.getElementById('from').value;let kgm3;if(f==='kgm3')kgm3=v;else if(f==='gcm3')kgm3=v*1000;else if(f==='lbft3')kgm3=v*16.0185;else kgm3=v*27679.9;document.getElementById('kgm3').textContent=kgm3.toFixed(4);document.getElementById('gcm3').textContent=(kgm3/1000).toFixed(6);document.getElementById('lbft3').textContent=(kgm3/16.0185).toFixed(4);document.getElementById('lbin3').textContent=(kgm3/27679.9).toFixed(6)}
convert();
"""
})

# ============================================================
# MISC FUN TOOLS
# ============================================================

TOOLS.append({
    "filename": "dice-roller.html",
    "title": "Dice Roller",
    "desc": "Roll virtual dice with any number of sides. Free online dice roller for D&D, board games and more.",
    "category": "Calculators",
    "keywords": "dice roller, roll dice, online dice, d6, d20, rpg dice roller, random dice",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Number of Dice</label><input type="number" id="count" value="2" min="1" max="100" oninput="roll()"></div>
  <div class="input-group"><label>Sides per Die</label><select id="sides" onchange="roll()"><option value="4">d4</option><option value="6" selected>d6</option><option value="8">d8</option><option value="10">d10</option><option value="12">d12</option><option value="20">d20</option><option value="100">d100</option></select></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="roll()">Roll!</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Results</div>
  <div class="value" id="dice" style="font-size:24px">3, 5</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Total: <strong id="total">8</strong></div>
</div>
""",
    "js": """
function roll(){const c=parseInt(document.getElementById('count').value)||1;const s=parseInt(document.getElementById('sides').value)||6;const results=[];let total=0;for(let i=0;i<c;i++){const r=Math.floor(Math.random()*s)+1;results.push(r);total+=r}document.getElementById('dice').textContent=results.join(', ');document.getElementById('total').textContent=total}
roll();
"""
})

TOOLS.append({
    "filename": "coin-flip.html",
    "title": "Coin Flip",
    "desc": "Flip a virtual coin for heads or tails. Free online coin flip simulator.",
    "category": "Calculators",
    "keywords": "coin flip, flip a coin, heads or tails, coin toss, random coin flip",
    "html": """
<div style="display:flex;gap:8px;margin-top:12px;justify-content:center"><button class="btn" onclick="flip()" style="font-size:18px;padding:16px 48px">Flip Coin</button></div>
<div class="result-box show" style="display:block;margin-top:16px;text-align:center">
  <div class="label">Result</div>
  <div class="value" id="result" style="font-size:32px">Heads</div>
</div>
<div style="margin-top:16px;text-align:center;font-size:14px;color:var(--text-soft)">
  <span>Heads: <strong id="heads">0</strong></span> &nbsp;|&nbsp;
  <span>Tails: <strong id="tails">0</strong></span> &nbsp;|&nbsp;
  <span>Total Flips: <strong id="total">0</strong></span>
</div>
""",
    "js": """
let h=0,t=0,n=0;function flip(){const r=Math.random()<0.5?'Heads':'Tails';document.getElementById('result').textContent=r;if(r==='Heads')h++;else t++;n++;document.getElementById('heads').textContent=h;document.getElementById('tails').textContent=t;document.getElementById('total').textContent=n}
flip();
"""
})

TOOLS.append({
    "filename": "password-strength-checker.html",
    "title": "Password Strength Checker",
    "desc": "Check password strength and security. Free online password strength tester with tips.",
    "category": "Developer Tools",
    "keywords": "password strength checker, password test, password security, strong password, password meter",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Password</label><input type="text" id="pw" value="" placeholder="Enter password to test..." oninput="check()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Strength</div>
  <div class="value" id="strength">Enter a password</div>
  <div style="margin-top:8px;height:8px;background:var(--border);border-radius:4px;overflow:hidden"><div id="bar" style="height:100%;width:0;background:#e53935;transition:all .3s"></div></div>
  <div style="margin-top:8px;font-size:13px;color:var(--text-soft)" id="tips"></div>
</div>
""",
    "js": """
function check(){const pw=document.getElementById('pw').value;if(!pw){document.getElementById('strength').textContent='Enter a password';document.getElementById('bar').style.width='0';document.getElementById('tips').innerHTML='';return}let score=0;const tips=[];if(pw.length>=8){score+=1}else{tips.push('Use at least 8 characters')}if(pw.length>=12){score+=1}if(/[a-z]/.test(pw)){score+=1}else{tips.push('Add lowercase letters')}if(/[A-Z]/.test(pw)){score+=1}else{tips.push('Add uppercase letters')}if(/[0-9]/.test(pw)){score+=1}else{tips.push('Add numbers')}if(/[^a-zA-Z0-9]/.test(pw)){score+=1}else{tips.push('Add special characters (!@#$)')}let label,color,width;if(score<=2){label='Weak';color='#e53935';width='25%'}else if(score<=3){label='Fair';color='#fb8c00';width='50%'}else if(score<=4){label='Good';color='#43a047';width='75%'}else{label='Strong';color='#2e7d32';width='100%'}document.getElementById('strength').textContent=label;document.getElementById('bar').style.width=width;document.getElementById('bar').style.background=color;document.getElementById('tips').innerHTML=tips.length?'Tips: '+tips.join(', '):'Great password!'}
"""
})

TOOLS.append({
    "filename": "email-validator.html",
    "title": "Email Validator",
    "desc": "Validate email addresses and check format. Free online email validation tool.",
    "category": "Developer Tools",
    "keywords": "email validator, email checker, validate email, email format checker, email verification",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Email Address</label><input type="text" id="email" value="test@example.com" oninput="validate()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Validation Result</div>
  <div class="value" id="result">Valid email format</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)" id="details"></div>
</div>
""",
    "js": """
function validate(){const e=document.getElementById('email').value.trim();if(!e){document.getElementById('result').textContent='Enter an email';document.getElementById('details').textContent='';return}const re=/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;const valid=re.test(e);document.getElementById('result').textContent=valid?'Valid email format':'Invalid email format';document.getElementById('result').style.color=valid?'#2e7d32':'#c62828';if(valid){const[at,domain]=e.split('@');document.getElementById('details').textContent='Local part: '+at+' | Domain: '+domain+' | Length: '+e.length}else{document.getElementById('details').textContent='Email must contain @ and a valid domain (e.g. user@example.com)'}}
validate();
"""
})

TOOLS.append({
    "filename": "bitwise-calculator.html",
    "title": "Bitwise Calculator",
    "desc": "Perform bitwise AND, OR, XOR, NOT, shift left and shift right operations. Free online bitwise calculator.",
    "category": "Developer Tools",
    "keywords": "bitwise calculator, bitwise and, bitwise or, bitwise xor, bit shift, binary calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Value A</label><input type="number" id="a" value="12" oninput="calc()"></div>
  <div class="input-group" style="max-width:80px"><label>Op</label><select id="op" onchange="calc()"><option value="and">AND</option><option value="or">OR</option><option value="xor">XOR</option><option value="lshift">&lt;&lt;</option><option value="rshift">&gt;&gt;</option></select></div>
  <div class="input-group"><label>Value B</label><input type="number" id="b" value="10" oninput="calc()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Result</div>
  <div class="value" id="dec">8</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">
    <div>Binary: <strong id="bin">1000</strong></div>
    <div>Hex: <strong id="hex">0x8</strong></div>
  </div>
</div>
""",
    "js": """
function calc(){const a=parseInt(document.getElementById('a').value)||0;const b=parseInt(document.getElementById('b').value)||0;const op=document.getElementById('op').value;let r;if(op==='and')r=a&b;else if(op==='or')r=a|b;else if(op==='xor')r=a^b;else if(op==='lshift')r=a<<b;else r=a>>b;document.getElementById('dec').textContent=r;document.getElementById('bin').textContent=(r>>>0).toString(2);document.getElementById('hex').textContent='0x'+(r>>>0).toString(16).toUpperCase()}
calc();
"""
})

# ============================================================
# MORE HEALTH
# ============================================================

TOOLS.append({
    "filename": "pregnancy-calculator.html",
    "title": "Pregnancy Due Date Calculator",
    "desc": "Calculate pregnancy due date and current week from last menstrual period. Free online pregnancy calculator.",
    "category": "Health Calculators",
    "keywords": "pregnancy calculator, due date calculator, pregnancy week, expected due date, pregnancy tracker",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Last Menstrual Period (LMP)</label><input type="date" id="lmp" value="2026-01-01" oninput="calcPreg()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Estimated Due Date</div>
  <div class="value" id="duedate">2026-10-08</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Current Week: <strong id="week">--</strong></span>
    <span>Days Pregnant: <strong id="days">--</strong></span>
    <span>Trimester: <strong id="tri">--</strong></div>
  </div>
</div>
""",
    "js": """
function calcPreg(){const lmp=new Date(document.getElementById('lmp').value);if(isNaN(lmp))return;const due=new Date(lmp);due.setDate(due.getDate()+280);document.getElementById('duedate').textContent=due.toISOString().slice(0,10);const now=new Date();const days=Math.floor((now-lmp)/86400000);const week=Math.floor(days/7);document.getElementById('days').textContent=Math.max(0,days);document.getElementById('week').textContent=Math.max(0,week)+' weeks';let tri;if(week<13)tri='First';else if(week<27)tri='Second';else tri='Third';document.getElementById('tri').textContent=tri}
calcPreg();
"""
})

TOOLS.append({
    "filename": "ovulation-calculator.html",
    "title": "Ovulation Calculator",
    "desc": "Calculate ovulation date and fertile window from menstrual cycle. Free online ovulation tracker.",
    "category": "Health Calculators",
    "keywords": "ovulation calculator, fertile window, ovulation date, fertility calculator, ovulation tracker",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Last Period Start Date</label><input type="date" id="lmp" value="2026-01-01" oninput="calcOv()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Cycle Length (days)</label><input type="number" id="cycle" value="28" oninput="calcOv()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Ovulation Date</div>
  <div class="value" id="ovdate">2026-01-15</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Fertile Window: <strong id="fertile">Jan 10 - Jan 15</strong></span>
    <span>Next Period: <strong id="next">Jan 29</strong></span>
  </div>
</div>
""",
    "js": """
function calcOv(){const lmp=new Date(document.getElementById('lmp').value);const c=parseInt(document.getElementById('cycle').value)||28;if(isNaN(lmp))return;const ov=new Date(lmp);ov.setDate(ov.getDate()+c-14);const fertileStart=new Date(ov);fertileStart.setDate(fertileStart.getDate()-5);const nextP=new Date(lmp);nextP.setDate(nextP.getDate()+c);const fmt=d=>d.toISOString().slice(0,10);const fmtShort=d=>d.toLocaleDateString('en-US',{month:'short',day:'numeric'});document.getElementById('ovdate').textContent=fmt(ov);document.getElementById('fertile').textContent=fmtShort(fertileStart)+' - '+fmtShort(ov);document.getElementById('next').textContent=fmtShort(nextP)}
calcOv();
"""
})

# ============================================================
# CSS TOOLS
# ============================================================

TOOLS.append({
    "filename": "css-border-radius-generator.html",
    "title": "CSS Border Radius Generator",
    "desc": "Generate CSS border-radius code with live preview. Free online CSS border radius generator.",
    "category": "Color Tools",
    "keywords": "css border radius generator, border radius, rounded corners, css generator, border radius code",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Top-Left (px)</label><input type="number" id="tl" value="10" oninput="gen()"></div>
  <div class="input-group"><label>Top-Right (px)</label><input type="number" id="tr" value="10" oninput="gen()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Bottom-Right (px)</label><input type="number" id="br" value="10" oninput="gen()"></div>
  <div class="input-group"><label>Bottom-Left (px)</label><input type="number" id="bl" value="10" oninput="gen()"></div>
</div>
<div style="margin-top:8px"><label style="font-size:14px;font-weight:normal"><input type="checkbox" id="link" checked onchange="toggleLink()"> Link all corners</label></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Preview</div>
  <div style="margin-top:12px;padding:40px;background:#f5f5f5;border-radius:8px;text-align:center">
    <div id="preview" style="width:150px;height:100px;background:#3366ff;border-radius:10px;margin:0 auto"></div>
  </div>
  <div style="margin-top:12px">
    <code id="code" style="display:block;padding:12px;background:var(--card);border-radius:6px;font-family:'Courier New',monospace;font-size:13px">border-radius: 10px;</code>
  </div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="copyCode()">Copy CSS</button></div>
""",
    "js": """
function gen(){const tl=document.getElementById('tl').value;const tr=document.getElementById('tr').value;const br=document.getElementById('br').value;const bl=document.getElementById('bl').value;if(document.getElementById('link').checked){const val=tl;document.getElementById('tr').value=val;document.getElementById('br').value=val;document.getElementById('bl').value=val;const css='border-radius: '+val+'px;';document.getElementById('preview').style.borderRadius=val+'px';document.getElementById('code').textContent=css;return}const css='border-radius: '+tl+'px '+tr+'px '+br+'px '+bl+'px;';document.getElementById('preview').style.borderRadius=tl+'px '+tr+'px '+br+'px '+bl+'px';document.getElementById('code').textContent=css}
function toggleLink(){gen()}
function copyCode(){navigator.clipboard.writeText(document.getElementById('code').textContent)}
gen();
"""
})

TOOLS.append({
    "filename": "css-flexbox-generator.html",
    "title": "CSS Flexbox Generator",
    "desc": "Generate CSS flexbox code with live preview. Free online CSS flexbox layout generator.",
    "category": "Color Tools",
    "keywords": "css flexbox generator, flexbox, css flex, flex direction, justify content, align items",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>flex-direction</label><select id="fd" onchange="gen()"><option value="row">row</option><option value="column">column</option><option value="row-reverse">row-reverse</option><option value="column-reverse">column-reverse</option></select></div>
  <div class="input-group"><label>justify-content</label><select id="jc" onchange="gen()"><option value="flex-start">flex-start</option><option value="center" selected>center</option><option value="flex-end">flex-end</option><option value="space-between">space-between</option><option value="space-around">space-around</option><option value="space-evenly">space-evenly</option></select></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>align-items</label><select id="ai" onchange="gen()"><option value="flex-start">flex-start</option><option value="center" selected>center</option><option value="flex-end">flex-end</option><option value="stretch">stretch</option></select></div>
  <div class="input-group"><label>gap (px)</label><input type="number" id="gap" value="10" oninput="gen()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Preview</div>
  <div id="preview" style="margin-top:12px;padding:16px;background:#f5f5f5;border-radius:8px;height:120px;display:flex;flex-direction:row;justify-content:center;align-items:center;gap:10px">
    <div style="width:40px;height:40px;background:#e53935;border-radius:4px"></div>
    <div style="width:40px;height:40px;background:#43a047;border-radius:4px"></div>
    <div style="width:40px;height:40px;background:#3366ff;border-radius:4px"></div>
  </div>
  <div style="margin-top:12px">
    <code id="code" style="display:block;padding:12px;background:var(--card);border-radius:6px;font-family:'Courier New',monospace;font-size:13px;white-space:pre-wrap"></code>
  </div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="copyCode()">Copy CSS</button></div>
""",
    "js": """
function gen(){const fd=document.getElementById('fd').value;const jc=document.getElementById('jc').value;const ai=document.getElementById('ai').value;const gap=document.getElementById('gap').value;const p=document.getElementById('preview');p.style.flexDirection=fd;p.style.justifyContent=jc;p.style.alignItems=ai;p.style.gap=gap+'px';document.getElementById('code').textContent='display: flex;\\nflex-direction: '+fd+';\\njustify-content: '+jc+';\\nalign-items: '+ai+';\\ngap: '+gap+'px;'}
function copyCode(){navigator.clipboard.writeText(document.getElementById('code').textContent)}
gen();
"""
})

# Generate all
print(f"Generating {len(TOOLS)} new tool pages...")
for t in TOOLS:
    make_page(t["filename"], t["title"], t["desc"], t["category"], t["keywords"], t["html"], t["js"], REL)

print(f"\nDone! Generated {len(TOOLS)} new pages.")
