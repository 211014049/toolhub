#!/usr/bin/env python3
"""Generate 40+ high-value tool pages for ToolHub."""
import os, json

OUT = os.path.join(os.path.dirname(__file__), "docs")
SITE_URL = "https://211014049.github.io/toolhub"

def slug(s):
    return s

def make_page(filename, title, desc, category, keywords, html_body, js_code, related_tools):
    """Generate a complete HTML page for a tool."""
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

# ============================================================
# TOOL DEFINITIONS
# ============================================================

TOOLS = []

# --- Finance Calculators ---

TOOLS.append({
    "filename": "loan-calculator.html",
    "title": "Loan Calculator",
    "desc": "Calculate monthly loan payments, total interest, and total cost. Free online loan payment calculator.",
    "category": "Finance Calculators",
    "keywords": "loan calculator, monthly payment calculator, loan payment, interest calculator, personal loan calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Loan Amount ($)</label><input type="number" id="principal" value="10000" oninput="calcLoan()"></div>
  <div class="input-group"><label>Annual Interest Rate (%)</label><input type="number" id="rate" value="5.5" step="0.1" oninput="calcLoan()"></div>
  <div class="input-group"><label>Loan Term (months)</label><input type="number" id="months" value="36" oninput="calcLoan()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Monthly Payment</div>
  <div class="value" id="monthly">$299.71</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Total Interest: <strong id="interest">$779.56</strong></span>
    <span>Total Paid: <strong id="total">$10,779.56</strong></span>
  </div>
</div>
""",
    "js": """
function calcLoan(){const p=parseFloat(document.getElementById('principal').value)||0;const r=(parseFloat(document.getElementById('rate').value)||0)/100/12;const n=parseInt(document.getElementById('months').value)||0;if(p>0&&r>0&&n>0){const m=p*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);const total=m*n;const interest=total-p;document.getElementById('monthly').textContent='$'+m.toFixed(2);document.getElementById('interest').textContent='$'+interest.toFixed(2);document.getElementById('total').textContent='$'+total.toFixed(2)}}
calcLoan();
"""
})

TOOLS.append({
    "filename": "mortgage-calculator.html",
    "title": "Mortgage Calculator",
    "desc": "Calculate monthly mortgage payments including principal, interest, taxes and insurance. Free online mortgage calculator.",
    "category": "Finance Calculators",
    "keywords": "mortgage calculator, home loan calculator, monthly mortgage payment, house payment calculator, mortgage estimator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Home Price ($)</label><input type="number" id="price" value="300000" oninput="calcMortgage()"></div>
  <div class="input-group"><label>Down Payment ($)</label><input type="number" id="down" value="60000" oninput="calcMortgage()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Interest Rate (%)</label><input type="number" id="rate" value="6.5" step="0.1" oninput="calcMortgage()"></div>
  <div class="input-group"><label>Loan Term (years)</label><input type="number" id="years" value="30" oninput="calcMortgage()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Monthly Payment</div>
  <div class="value" id="monthly">$1,516.67</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Loan Amount: <strong id="loanamt">$240,000</strong></span>
    <span>Total Interest: <strong id="interest">$306,001</strong></span>
  </div>
</div>
""",
    "js": """
function calcMortgage(){const price=parseFloat(document.getElementById('price').value)||0;const down=parseFloat(document.getElementById('down').value)||0;const r=(parseFloat(document.getElementById('rate').value)||0)/100/12;const n=(parseInt(document.getElementById('years').value)||0)*12;const loan=price-down;if(loan>0&&r>0&&n>0){const m=loan*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);const total=m*n;const interest=total-loan;document.getElementById('monthly').textContent='$'+m.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});document.getElementById('loanamt').textContent='$'+loan.toLocaleString('en-US');document.getElementById('interest').textContent='$'+Math.round(interest).toLocaleString('en-US')}}
calcMortgage();
"""
})

TOOLS.append({
    "filename": "sales-tax-calculator.html",
    "title": "Sales Tax Calculator",
    "desc": "Calculate sales tax and total price including tax. Free online sales tax calculator for any state or country.",
    "category": "Finance Calculators",
    "keywords": "sales tax calculator, tax calculator, vat calculator, price with tax, tax included calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Amount Before Tax ($)</label><input type="number" id="amount" value="100" oninput="calcTax()"></div>
  <div class="input-group"><label>Tax Rate (%)</label><input type="number" id="rate" value="8.25" step="0.01" oninput="calcTax()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Total After Tax</div>
  <div class="value" id="total">$108.25</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Tax Amount: <strong id="tax">$8.25</strong></div>
</div>
""",
    "js": """
function calcTax(){const a=parseFloat(document.getElementById('amount').value)||0;const r=parseFloat(document.getElementById('rate').value)||0;const tax=a*r/100;document.getElementById('tax').textContent='$'+tax.toFixed(2);document.getElementById('total').textContent='$'+(a+tax).toFixed(2)}
calcTax();
"""
})

TOOLS.append({
    "filename": "simple-interest-calculator.html",
    "title": "Simple Interest Calculator",
    "desc": "Calculate simple interest on loans and investments. Free online simple interest calculator.",
    "category": "Finance Calculators",
    "keywords": "simple interest calculator, interest calculator, loan interest, investment interest, si calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Principal ($)</label><input type="number" id="principal" value="5000" oninput="calcSI()"></div>
  <div class="input-group"><label>Rate (%)</label><input type="number" id="rate" value="5" step="0.1" oninput="calcSI()"></div>
  <div class="input-group"><label>Time (years)</label><input type="number" id="time" value="3" oninput="calcSI()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Simple Interest</div>
  <div class="value" id="interest">$750.00</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Total Amount: <strong id="total">$5,750.00</strong></div>
</div>
""",
    "js": """
function calcSI(){const p=parseFloat(document.getElementById('principal').value)||0;const r=parseFloat(document.getElementById('rate').value)||0;const t=parseFloat(document.getElementById('time').value)||0;const si=p*r*t/100;document.getElementById('interest').textContent='$'+si.toFixed(2);document.getElementById('total').textContent='$'+(p+si).toFixed(2)}
calcSI();
"""
})

TOOLS.append({
    "filename": "roi-calculator.html",
    "title": "ROI Calculator",
    "desc": "Calculate Return on Investment (ROI) and annualized return. Free online ROI calculator for investments.",
    "category": "Finance Calculators",
    "keywords": "roi calculator, return on investment, investment return, annualized return, roi percentage",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Initial Investment ($)</label><input type="number" id="initial" value="10000" oninput="calcROI()"></div>
  <div class="input-group"><label>Final Value ($)</label><input type="number" id="final" value="15000" oninput="calcROI()"></div>
  <div class="input-group"><label>Time (years)</label><input type="number" id="years" value="2" step="0.5" oninput="calcROI()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Return on Investment</div>
  <div class="value" id="roi">50.00%</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Annualized Return: <strong id="annual">22.47%</strong> | Profit: <strong id="profit">$5,000</strong></div>
</div>
""",
    "js": """
function calcROI(){const i=parseFloat(document.getElementById('initial').value)||0;const f=parseFloat(document.getElementById('final').value)||0;const y=parseFloat(document.getElementById('years').value)||0;if(i>0){const roi=(f-i)/i*100;const annual=y>0?(Math.pow(f/i,1/y)-1)*100:0;document.getElementById('roi').textContent=roi.toFixed(2)+'%';document.getElementById('annual').textContent=annual.toFixed(2)+'%';document.getElementById('profit').textContent='$'+(f-i).toLocaleString('en-US')}}}
calcROI();
"""
})

TOOLS.append({
    "filename": "car-payment-calculator.html",
    "title": "Car Payment Calculator",
    "desc": "Calculate monthly car loan payments, total interest and total cost. Free online auto loan calculator.",
    "category": "Finance Calculators",
    "keywords": "car payment calculator, auto loan calculator, car loan estimator, monthly car payment, vehicle payment calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Vehicle Price ($)</label><input type="number" id="price" value="25000" oninput="calcCar()"></div>
  <div class="input-group"><label>Down Payment ($)</label><input type="number" id="down" value="5000" oninput="calcCar()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Interest Rate (%)</label><input type="number" id="rate" value="4.5" step="0.1" oninput="calcCar()"></div>
  <div class="input-group"><label>Loan Term (months)</label><input type="number" id="months" value="60" oninput="calcCar()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Monthly Payment</div>
  <div class="value" id="monthly">$372.86</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Total Interest: <strong id="interest">$2,371.65</strong></span>
    <span>Total Cost: <strong id="total">$22,371.65</strong></span>
  </div>
</div>
""",
    "js": """
function calcCar(){const p=parseFloat(document.getElementById('price').value)-parseFloat(document.getElementById('down').value)||0;const r=(parseFloat(document.getElementById('rate').value)||0)/100/12;const n=parseInt(document.getElementById('months').value)||0;if(p>0&&r>0&&n>0){const m=p*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);const total=m*n;document.getElementById('monthly').textContent='$'+m.toFixed(2);document.getElementById('interest').textContent='$'+(total-p).toFixed(2);document.getElementById('total').textContent='$'+total.toFixed(2)}} 
calcCar();
"""
})

TOOLS.append({
    "filename": "income-tax-calculator.html",
    "title": "Income Tax Calculator",
    "desc": "Estimate federal income tax based on your annual income. Free online income tax calculator.",
    "category": "Finance Calculators",
    "keywords": "income tax calculator, tax estimator, federal tax, take home pay, salary calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Annual Income ($)</label><input type="number" id="income" value="75000" oninput="calcTax()"></div>
  <div class="input-group"><label>Filing Status</label>
    <select id="status" onchange="calcTax()">
      <option value="single">Single</option>
      <option value="married">Married Filing Jointly</option>
      <option value="head">Head of Household</option>
    </select>
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Estimated Tax</div>
  <div class="value" id="tax">$12,183.50</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Effective Rate: <strong id="rate">16.24%</strong> | Take Home: <strong id="net">$62,816.50</strong></div>
</div>
<div style="margin-top:12px;font-size:12px;color:var(--text-soft)">Note: Simplified estimate using 2024 federal brackets. Does not include deductions, credits, or state tax.</div>
""",
    "js": """
function calcTax(){const inc=parseFloat(document.getElementById('income').value)||0;const st=document.getElementById('status').value;let brackets;if(st==='single')brackets=[[0,0.1],[11600,0.12],[47150,0.22],[100525,0.24],[191950,0.32],[243725,0.35],[609350,0.37]];else if(st==='married')brackets=[[0,0.1],[23200,0.12],[94300,0.22],[201050,0.24],[383900,0.32],[487450,0.35],[731200,0.37]];else brackets=[[0,0.1],[16550,0.12],[63100,0.22],[100500,0.24],[191950,0.32],[243700,0.35],[609350,0.37]];let tax=0;let prev=0;for(const[br,rate]of brackets){if(inc>br){tax+=(Math.min(inc,br+9999999)-prev)*rate;prev=br}else{tax+=(inc-prev)*rate;break}}document.getElementById('tax').textContent='$'+tax.toFixed(2);document.getElementById('rate').textContent=(inc>0?(tax/inc*100).toFixed(2):0)+'%';document.getElementById('net').textContent='$'+(inc-tax).toFixed(2)}
calcTax();
"""
})

# --- Math Calculators ---

TOOLS.append({
    "filename": "scientific-calculator.html",
    "title": "Scientific Calculator",
    "desc": "Free online scientific calculator with trigonometric, logarithmic and exponential functions.",
    "category": "Math Calculators",
    "keywords": "scientific calculator, online calculator, math calculator, sin cos tan calculator, logarithm calculator",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%">
    <label>Expression</label>
    <input type="text" id="expr" value="sin(45) + log(100)" style="font-family:'Courier New',monospace" onkeypress="if(event.key==='Enter')calcSci()">
  </div>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn" onclick="calcSci()">Calculate</button>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Result</div>
  <div class="value" id="result">2.7071</div>
</div>
<div style="margin-top:12px;font-size:12px;color:var(--text-soft)">Supports: + - * / ^ ( ) sin cos tan asin acos atan log ln sqrt abs exp pi e</div>
""",
    "js": """
function calcSci(){try{let e=document.getElementById('expr').value;e=e.replace(/\\^/g,'**');e=e.replace(/\\bsin\\(/g,'Math.sin(');e=e.replace(/\\bcos\\(/g,'Math.cos(');e=e.replace(/\\btan\\(/g,'Math.tan(');e=e.replace(/\\basin\\(/g,'Math.asin(');e=e.replace(/\\bacos\\(/g,'Math.acos(');e=e.replace(/\\batan\\(/g,'Math.atan(');e=e.replace(/\\blog\\(/g,'Math.log10(');e=e.replace(/\\bln\\(/g,'Math.log(');e=e.replace(/\\bsqrt\\(/g,'Math.sqrt(');e=e.replace(/\\babs\\(/g,'Math.abs(');e=e.replace(/\\bexp\\(/g,'Math.exp(');e=e.replace(/\\bpi\\b/g,'Math.PI');e=e.replace(/\\be\\b/g,'Math.E');const r=Function('return '+e)();document.getElementById('result').textContent=typeof r==='number'?r.toString():'Error'}catch(err){document.getElementById('result').textContent='Error: '+err.message}}
"""
})

TOOLS.append({
    "filename": "fraction-calculator.html",
    "title": "Fraction Calculator",
    "desc": "Add, subtract, multiply and divide fractions. Free online fraction calculator with step-by-step results.",
    "category": "Math Calculators",
    "keywords": "fraction calculator, adding fractions, subtracting fractions, multiplying fractions, dividing fractions",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Fraction 1 (a/b)</label><input type="text" id="f1" value="1/4" style="font-family:'Courier New',monospace"></div>
  <div class="input-group" style="max-width:60px"><label>Op</label>
    <select id="op"><option value="+">+</option><option value="-">-</option><option value="*">&times;</option><option value="/">/</option></select>
  </div>
  <div class="input-group"><label>Fraction 2 (c/d)</label><input type="text" id="f2" value="3/8" style="font-family:'Courier New',monospace"></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="calcFrac()">Calculate</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Result</div>
  <div class="value" id="result">5/8</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Decimal: <strong id="decimal">0.625</strong></div>
</div>
""",
    "js": """
function gcd(a,b){return b===0?a:gcd(b,a%b)}
function calcFrac(){try{const p1=document.getElementById('f1').value.split('/').map(Number);const p2=document.getElementById('f2').value.split('/').map(Number);let n1=p1.length===2?p1[0]/p1[1]:p1[0];let d1=p1.length===2?p1[1]:1;let n2=p2.length===2?p2[0]/p2[1]:p2[0];let d2=p2.length===2?p2[1]:1;const op=document.getElementById('op').value;let n,d;if(op==='+'){n=n1*d2+n2*d1;d=d1*d2}else if(op==='-'){n=n1*d2-n2*d1;d=d1*d2}else if(op==='*'){n=n1*n2;d=d1*d2}else{n=n1*d2;d=d1*n2}if(d<0){d=-d;n=-n}const g=gcd(Math.abs(n),Math.abs(d));n=n/g;d=d/g;document.getElementById('result').textContent=n+'/'+d;document.getElementById('decimal').textContent=(n/d).toFixed(6)}catch(e){document.getElementById('result').textContent='Error'}}
"""
})

TOOLS.append({
    "filename": "quadratic-equation-solver.html",
    "title": "Quadratic Equation Solver",
    "desc": "Solve quadratic equations ax^2 + bx + c = 0. Free online quadratic formula calculator with steps.",
    "category": "Math Calculators",
    "keywords": "quadratic equation solver, quadratic formula, quadratic calculator, solve quadratic, discriminant",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>a (x^2)</label><input type="number" id="a" value="1" step="any" oninput="calcQuad()"></div>
  <div class="input-group"><label>b (x)</label><input type="number" id="b" value="-3" step="any" oninput="calcQuad()"></div>
  <div class="input-group"><label>c</label><input type="number" id="c" value="2" step="any" oninput="calcQuad()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Solutions</div>
  <div class="value" id="result">x = 2, x = -1</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Discriminant: <strong id="disc">1</strong></div>
</div>
""",
    "js": """
function calcQuad(){const a=parseFloat(document.getElementById('a').value)||0;const b=parseFloat(document.getElementById('b').value)||0;const c=parseFloat(document.getElementById('c').value)||0;if(a===0){document.getElementById('result').textContent='a cannot be 0';return}const disc=b*b-4*a*c;document.getElementById('disc').textContent=disc.toFixed(4);if(disc<0){const re=-b/(2*a);const im=Math.sqrt(-disc)/(2*a);document.getElementById('result').textContent='x = '+re.toFixed(4)+' + '+im.toFixed(4)+'i, x = '+re.toFixed(4)+' - '+im.toFixed(4)+'i'}else if(disc===0){const x=-b/(2*a);document.getElementById('result').textContent='x = '+x.toFixed(4)+' (double root)'}else{const x1=(-b+Math.sqrt(disc))/(2*a);const x2=(-b-Math.sqrt(disc))/(2*a);document.getElementById('result').textContent='x = '+x1.toFixed(4)+', x = '+x2.toFixed(4)}}
calcQuad();
"""
})

TOOLS.append({
    "filename": "percentage-increase-calculator.html",
    "title": "Percentage Increase Calculator",
    "desc": "Calculate percentage increase or decrease between two values. Free online percent change calculator.",
    "category": "Math Calculators",
    "keywords": "percentage increase calculator, percent change, percentage decrease, percent difference, growth rate",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Original Value</label><input type="number" id="original" value="100" oninput="calcPctInc()"></div>
  <div class="input-group"><label>New Value</label><input type="number" id="newval" value="150" oninput="calcPctInc()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Percentage Change</div>
  <div class="value" id="result">+50%</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Change: <strong id="change">+50</strong></div>
</div>
""",
    "js": """
function calcPctInc(){const o=parseFloat(document.getElementById('original').value)||0;const n=parseFloat(document.getElementById('newval').value)||0;if(o!==0){const pct=(n-o)/o*100;const sign=pct>=0?'+':'';document.getElementById('result').textContent=sign+pct.toFixed(2)+'%';document.getElementById('change').textContent=sign+(n-o).toFixed(2)}}
calcPctInc();
"""
})

TOOLS.append({
    "filename": "ratio-calculator.html",
    "title": "Ratio Calculator",
    "desc": "Simplify ratios, scale ratios and find equivalent ratios. Free online ratio calculator.",
    "category": "Math Calculators",
    "keywords": "ratio calculator, simplify ratio, equivalent ratio, ratio solver, proportion calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>First Number (A)</label><input type="number" id="a" value="12" oninput="calcRatio()"></div>
  <div class="input-group"><label>Second Number (B)</label><input type="number" id="b" value="8" oninput="calcRatio()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Simplified Ratio</div>
  <div class="value" id="result">3 : 2</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">A/B = <strong id="decimal">1.5</strong></div>
</div>
""",
    "js": """
function gcd(a,b){return b===0?a:gcd(b,a%b)}
function calcRatio(){const a=parseInt(document.getElementById('a').value)||0;const b=parseInt(document.getElementById('b').value)||0;if(a===0&&b===0){document.getElementById('result').textContent='0 : 0';return}const g=gcd(Math.abs(a),Math.abs(b));const sa=a/g;const sb=b/g;document.getElementById('result').textContent=sa+' : '+sb;document.getElementById('decimal').textContent=b!==0?(a/b).toFixed(4):'undefined'}
calcRatio();
"""
})

TOOLS.append({
    "filename": "gcd-lcm-calculator.html",
    "title": "GCD and LCM Calculator",
    "desc": "Find the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of any numbers. Free online GCD LCM calculator.",
    "category": "Math Calculators",
    "keywords": "gcd calculator, lcm calculator, greatest common divisor, least common multiple, hcf calculator",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Numbers (comma separated)</label><input type="text" id="nums" value="12, 18, 24" oninput="calcGCDLCM()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Results</div>
  <div class="value" id="gcd">GCD: 6</div>
  <div style="margin-top:4px;font-size:16px;color:var(--text)" id="lcm">LCM: 72</div>
</div>
""",
    "js": """
function gcd2(a,b){return b===0?a:gcd2(b,a%b)}
function lcm2(a,b){return a*b/gcd2(a,b)}
function calcGCDLCM(){const nums=document.getElementById('nums').value.split(',').map(s=>parseInt(s.trim())).filter(n=>!isNaN(n));if(nums.length<1)return;let g=nums[0];for(let i=1;i<nums.length;i++)g=gcd2(g,nums[i]);let l=nums[0];for(let i=1;i<nums.length;i++)l=lcm2(l,nums[i]);document.getElementById('gcd').textContent='GCD: '+g;document.getElementById('lcm').textContent='LCM: '+l}
calcGCDLCM();
"""
})

TOOLS.append({
    "filename": "number-to-words.html",
    "title": "Number to Words Converter",
    "desc": "Convert any number to English words. Free online number to text converter for checks and documents.",
    "category": "Math Calculators",
    "keywords": "number to words, number to text, write number in words, number spelling, check amount in words",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Number</label><input type="number" id="num" value="12345" oninput="convertNum()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">In Words</div>
  <div class="value" id="result" style="font-size:20px">Twelve Thousand Three Hundred Forty-Five</div>
</div>
""",
    "js": """
const ones=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'];const tens=['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'];const scales=['','Thousand','Million','Billion','Trillion'];
function threeDigits(n){let w='';if(n>=100){w+=ones[Math.floor(n/100)]+' Hundred ';n%=100}if(n>=20){w+=tens[Math.floor(n/10)];if(n%10)w+='-'+ones[n%10]}else{w+=ones[n]}return w.trim()}
function convertNum(){const n=parseInt(document.getElementById('num').value);if(isNaN(n)){document.getElementById('result').textContent='';return}if(n===0){document.getElementById('result').textContent='Zero';return}let num=Math.abs(n);let words=n<0?'Negative ':'';let scaleIdx=0;let parts=[];while(num>0){const chunk=num%1000;if(chunk>0){parts.unshift(threeDigits(chunk)+(scales[scaleIdx]?' '+scales[scaleIdx]:''))}num=Math.floor(num/1000);scaleIdx++}document.getElementById('result').textContent=parts.join(' ')}
convertNum();
"""
})

# --- Number Base Converters ---

def make_base_converter(filename, title, desc, from_base, to_base, from_label, to_label, keywords):
    return {
        "filename": filename,
        "title": title,
        "desc": desc,
        "category": "Number Base Converters",
        "keywords": keywords,
        "html": f"""
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>{from_label}</label><input type="text" id="input" value="255" oninput="convertBase()" style="font-family:'Courier New',monospace"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">{to_label}</div>
  <div class="value" id="result" style="font-family:'Courier New',monospace">FF</div>
</div>
""",
        "js": f"""
function convertBase(){{try{{const v=document.getElementById('input').value.trim();if(!v){{document.getElementById('result').textContent='';return}}const dec=parseInt(v,{from_base});if(isNaN(dec)){{document.getElementById('result').textContent='Invalid input';return}}document.getElementById('result').textContent=dec.toString({to_base}).toUpperCase()}}catch(e){{document.getElementById('result').textContent='Error'}}}}
convertBase();
"""
    }

TOOLS.append(make_base_converter("decimal-to-binary.html", "Decimal to Binary", "Convert decimal numbers to binary. Free online decimal to binary converter.", 10, 2, "Decimal", "Binary", "decimal to binary, decimal converter, binary converter, number base, decimal to bin"))
TOOLS.append(make_base_converter("binary-to-decimal.html", "Binary to Decimal", "Convert binary numbers to decimal. Free online binary to decimal converter.", 2, 10, "Binary", "Decimal", "binary to decimal, binary converter, decimal converter, number base, bin to dec"))
TOOLS.append(make_base_converter("decimal-to-hex.html", "Decimal to Hex", "Convert decimal numbers to hexadecimal. Free online decimal to hex converter.", 10, 16, "Decimal", "Hexadecimal", "decimal to hex, decimal to hexadecimal, hex converter, number base converter"))
TOOLS.append(make_base_converter("hex-to-decimal.html", "Hex to Decimal", "Convert hexadecimal numbers to decimal. Free online hex to decimal converter.", 16, 10, "Hexadecimal", "Decimal", "hex to decimal, hexadecimal to decimal, hex converter, number base converter"))
TOOLS.append(make_base_converter("decimal-to-octal.html", "Decimal to Octal", "Convert decimal numbers to octal. Free online decimal to octal converter.", 10, 8, "Decimal", "Octal", "decimal to octal, octal converter, number base, decimal to oct"))
TOOLS.append(make_base_converter("binary-to-hex.html", "Binary to Hex", "Convert binary numbers to hexadecimal. Free online binary to hex converter.", 2, 16, "Binary", "Hexadecimal", "binary to hex, binary to hexadecimal, bin to hex, number base converter"))
TOOLS.append(make_base_converter("hex-to-binary.html", "Hex to Binary", "Convert hexadecimal numbers to binary. Free online hex to binary converter.", 16, 2, "Hexadecimal", "Binary", "hex to binary, hexadecimal to binary, hex to bin, number base converter"))
TOOLS.append(make_base_converter("binary-to-octal.html", "Binary to Octal", "Convert binary numbers to octal. Free online binary to octal converter.", 2, 8, "Binary", "Octal", "binary to octal, bin to oct, number base converter, binary conversion"))
TOOLS.append(make_base_converter("octal-to-decimal.html", "Octal to Decimal", "Convert octal numbers to decimal. Free online octal to decimal converter.", 8, 10, "Octal", "Decimal", "octal to decimal, octal converter, number base, oct to dec"))

# --- Roman Numeral Converter ---

TOOLS.append({
    "filename": "roman-numeral-converter.html",
    "title": "Roman Numeral Converter",
    "desc": "Convert between Roman numerals and numbers. Free online Roman numeral translator.",
    "category": "Number Base Converters",
    "keywords": "roman numeral converter, roman numerals, roman to number, number to roman, roman numeral translator",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Number (1-3999)</label><input type="number" id="num" value="2024" min="1" max="3999" oninput="toRoman()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Roman Numeral</div>
  <div class="value" id="roman">MMXXIV</div>
</div>
<div style="margin-top:16px;border-top:1px solid var(--border);padding-top:16px">
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Roman Numeral</label><input type="text" id="rom" value="MMXXIV" oninput="fromRoman()" style="font-family:'Courier New',monospace"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Number</div>
  <div class="value" id="numout">2024</div>
</div>
</div>
""",
    "js": """
function toRoman(){const vals=[1000,900,500,400,100,90,50,40,10,9,5,4,1];const syms=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'];let n=parseInt(document.getElementById('num').value)||0;if(n<1||n>3999){document.getElementById('roman').textContent='Out of range';return}let r='';for(let i=0;i<vals.length;i++){while(n>=vals[i]){r+=syms[i];n-=vals[i]}}document.getElementById('roman').textContent=r}
function fromRoman(){const s=document.getElementById('rom').value.toUpperCase();const map={M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1};let n=0;let i=0;while(i<s.length){if(i+1<s.length&&map[s.substring(i,i+2)]){n+=map[s.substring(i,i+2)];i+=2}else{if(map[s[i]]){n+=map[s[i]];i++}else{i++}}}document.getElementById('numout').textContent=n}
toRoman();fromRoman();
"""
})

# --- Text to Binary and Binary to Text ---

TOOLS.append({
    "filename": "text-to-binary.html",
    "title": "Text to Binary Converter",
    "desc": "Convert text to binary code (ASCII). Free online text to binary translator.",
    "category": "Number Base Converters",
    "keywords": "text to binary, text to binary converter, ascii to binary, binary translator, text to bits",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Text Input</label><textarea id="input" placeholder="Hello World" oninput="textToBinary()">Hello</textarea></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Binary Output</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0;color:var(--text)">01001000 01100101 01101100 01101100 01101111</pre>
</div>
""",
    "js": """
function textToBinary(){const t=document.getElementById('input').value;let r='';for(let i=0;i<t.length;i++){r+=t.charCodeAt(i).toString(2).padStart(8,'0')+' '}document.getElementById('output').textContent=r.trim()}
textToBinary();
"""
})

TOOLS.append({
    "filename": "binary-to-text.html",
    "title": "Binary to Text Converter",
    "desc": "Convert binary code to readable text. Free online binary to text translator.",
    "category": "Number Base Converters",
    "keywords": "binary to text, binary to text converter, binary translator, binary decoder, ascii to text",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Binary Input (space separated)</label><textarea id="input" placeholder="01001000 01100101 01101100 01101100 01101111" oninput="binaryToText()">01001000 01100101 01101100 01101100 01101111</textarea></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Text Output</div>
  <div class="value" id="output" style="word-break:break-all">Hello</div>
</div>
""",
    "js": """
function binaryToText(){const parts=document.getElementById('input').value.trim().split(/\\s+/);let r='';for(const p of parts){if(p.length>0){const c=parseInt(p,2);if(!isNaN(c))r+=String.fromCharCode(c)}}document.getElementById('output').textContent=r}
binaryToText();
"""
})

# --- Date/Time Tools ---

TOOLS.append({
    "filename": "date-difference-calculator.html",
    "title": "Date Difference Calculator",
    "desc": "Calculate the difference between two dates in days, weeks, months and years. Free online date calculator.",
    "category": "Date & Time Tools",
    "keywords": "date difference calculator, days between dates, date duration, how many days between dates, date gap",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Start Date</label><input type="date" id="start" value="2026-01-01" oninput="calcDate()"></div>
  <div class="input-group"><label>End Date</label><input type="date" id="end" value="2026-12-31" oninput="calcDate()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Date Difference</div>
  <div class="value" id="days">364 days</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Weeks: <strong id="weeks">52</strong></span>
    <span>Months: <strong id="months">11</strong></span>
    <span>Years: <strong id="years">0.997</strong></span>
  </div>
</div>
""",
    "js": """
function calcDate(){const s=new Date(document.getElementById('start').value);const e=new Date(document.getElementById('end').value);if(isNaN(s)||isNaN(e))return;const ms=e-s;const days=Math.floor(ms/86400000);document.getElementById('days').textContent=days+' days';document.getElementById('weeks').textContent=Math.floor(days/7);document.getElementById('months').textContent=Math.floor(days/30.44);document.getElementById('years').textContent=(days/365.25).toFixed(3)}
calcDate();
"""
})

TOOLS.append({
    "filename": "countdown-timer.html",
    "title": "Countdown Timer",
    "desc": "Count down to any date and time. Free online countdown timer for events and deadlines.",
    "category": "Date & Time Tools",
    "keywords": "countdown timer, countdown, days until, time until, event countdown",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Target Date & Time</label><input type="datetime-local" id="target" value="2026-12-31T23:59" oninput="startCountdown()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Time Remaining</div>
  <div class="value" id="result" style="font-size:28px">--</div>
  <div style="display:flex;gap:16px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Days: <strong id="d">--</strong></span>
    <span>Hours: <strong id="h">--</strong></span>
    <span>Min: <strong id="m">--</strong></span>
    <span>Sec: <strong id="s">--</strong></span>
  </div>
</div>
""",
    "js": """
let timerId=null;
function startCountdown(){if(timerId)clearInterval(timerId);updateCountdown();timerId=setInterval(updateCountdown,1000)}
function updateCountdown(){const t=new Date(document.getElementById('target').value);if(isNaN(t)){document.getElementById('result').textContent='Invalid date';return}const now=new Date();let diff=t-now;if(diff<0){document.getElementById('result').textContent='Time has passed!';document.getElementById('d').textContent='0';document.getElementById('h').textContent='0';document.getElementById('m').textContent='0';document.getElementById('s').textContent='0';return}const d=Math.floor(diff/86400000);const h=Math.floor((diff%86400000)/3600000);const m=Math.floor((diff%3600000)/60000);const s=Math.floor((diff%60000)/1000);document.getElementById('result').textContent=d+'d '+h+'h '+m+'m '+s+'s';document.getElementById('d').textContent=d;document.getElementById('h').textContent=h;document.getElementById('m').textContent=m;document.getElementById('s').textContent=s}
startCountdown();
"""
})

TOOLS.append({
    "filename": "working-days-calculator.html",
    "title": "Working Days Calculator",
    "desc": "Calculate the number of working days (business days) between two dates. Free online business day calculator.",
    "category": "Date & Time Tools",
    "keywords": "working days calculator, business days, business day calculator, work days, weekdays between dates",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Start Date</label><input type="date" id="start" value="2026-01-01" oninput="calcWorkDays()"></div>
  <div class="input-group"><label>End Date</label><input type="date" id="end" value="2026-01-31" oninput="calcWorkDays()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Working Days</div>
  <div class="value" id="workdays">22</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Total Days: <strong id="total">31</strong></span>
    <span>Weekends: <strong id="weekends">9</strong></span>
  </div>
</div>
""",
    "js": """
function calcWorkDays(){const s=new Date(document.getElementById('start').value);const e=new Date(document.getElementById('end').value);if(isNaN(s)||isNaN(e))return;let work=0,total=0,weekend=0;let d=new Date(s);while(d<=e){total++;const day=d.getDay();if(day===0||day===6){weekend++}else{work++}d.setDate(d.getDate()+1)}document.getElementById('workdays').textContent=work;document.getElementById('total').textContent=total;document.getElementById('weekends').textContent=weekend}
calcWorkDays();
"""
})

# --- Health Calculators ---

TOOLS.append({
    "filename": "calorie-calculator.html",
    "title": "Calorie Calculator",
    "desc": "Calculate daily calorie needs (TDEE) based on age, weight, height and activity level. Free online calorie calculator.",
    "category": "Health Calculators",
    "keywords": "calorie calculator, tdee calculator, daily calorie needs, bmr calculator, maintenance calories",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Age</label><input type="number" id="age" value="25" oninput="calcCal()"></div>
  <div class="input-group"><label>Gender</label><select id="gender" onchange="calcCal()"><option value="male">Male</option><option value="female">Female</option></select></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Weight (kg)</label><input type="number" id="weight" value="70" oninput="calcCal()"></div>
  <div class="input-group"><label>Height (cm)</label><input type="number" id="height" value="170" oninput="calcCal()"></div>
</div>
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Activity Level</label>
    <select id="activity" onchange="calcCal()">
      <option value="1.2">Sedentary (little or no exercise)</option>
      <option value="1.375">Lightly active (1-3 days/week)</option>
      <option value="1.55" selected>Moderately active (3-5 days/week)</option>
      <option value="1.725">Very active (6-7 days/week)</option>
      <option value="1.9">Extra active (physical job)</option>
    </select>
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Daily Calories (TDEE)</div>
  <div class="value" id="tdee">2,414</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>BMR: <strong id="bmr">1,557</strong></span>
    <span>Lose Weight: <strong id="lose">1,914</strong></span>
    <span>Gain Weight: <strong id="gain">2,914</strong></span>
  </div>
</div>
""",
    "js": """
function calcCal(){const age=parseInt(document.getElementById('age').value)||0;const wt=parseFloat(document.getElementById('weight').value)||0;const ht=parseFloat(document.getElementById('height').value)||0;const g=document.getElementById('gender').value;const a=parseFloat(document.getElementById('activity').value);let bmr;if(g==='male')bmr=10*wt+6.25*ht-5*age+5;else bmr=10*wt+6.25*ht-5*age-161;const tdee=bmr*a;document.getElementById('bmr').textContent=Math.round(bmr).toLocaleString();document.getElementById('tdee').textContent=Math.round(tdee).toLocaleString();document.getElementById('lose').textContent=Math.round(tdee*0.79).toLocaleString();document.getElementById('gain').textContent=Math.round(tdee*1.21).toLocaleString()}
calcCal();
"""
})

TOOLS.append({
    "filename": "ideal-weight-calculator.html",
    "title": "Ideal Weight Calculator",
    "desc": "Calculate ideal body weight based on height and gender using multiple formulas. Free online ideal weight calculator.",
    "category": "Health Calculators",
    "keywords": "ideal weight calculator, healthy weight, target weight, ideal body weight, weight goal calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Gender</label><select id="gender" onchange="calcIW()"><option value="male">Male</option><option value="female">Female</option></select></div>
  <div class="input-group"><label>Height (cm)</label><input type="number" id="height" value="170" oninput="calcIW()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Ideal Weight Range</div>
  <div class="value" id="result">63.4 - 71.6 kg</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Devine: <strong id="devine">67.1 kg</strong> | Robinson: <strong id="rob">63.4 kg</strong> | Miller: <strong id="mil">66.0 kg</strong></div>
</div>
""",
    "js": """
function calcIW(){const h=parseFloat(document.getElementById('height').value)||0;const g=document.getElementById('gender').value;const inchOver152=(h-152.4)/2.54;if(inchOver152<0){document.getElementById('result').textContent='Height too low';return}let devine,rob,mil;if(g==='male'){devine=50+2.3*inchOver152;rob=52+1.9*inchOver152;mil=56.2+1.41*inchOver152}else{devine=45.5+2.3*inchOver152;rob=49+1.7*inchOver152;mil=53.1+1.36*inchOver152}const low=Math.min(devine,rob,mil);const high=Math.max(devine,rob,mil);document.getElementById('result').textContent=low.toFixed(1)+' - '+high.toFixed(1)+' kg';document.getElementById('devine').textContent=devine.toFixed(1)+' kg';document.getElementById('rob').textContent=rob.toFixed(1)+' kg';document.getElementById('mil').textContent=mil.toFixed(1)+' kg'}
calcIW();
"""
})

TOOLS.append({
    "filename": "body-fat-calculator.html",
    "title": "Body Fat Calculator",
    "desc": "Calculate body fat percentage using the U.S. Navy method. Free online body fat calculator.",
    "category": "Health Calculators",
    "keywords": "body fat calculator, body fat percentage, fat calculator, navy body fat, body composition",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Gender</label><select id="gender" onchange="calcBF()"><option value="male">Male</option><option value="female">Female</option></select></div>
  <div class="input-group"><label>Height (cm)</label><input type="number" id="height" value="170" oninput="calcBF()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Neck Circumference (cm)</label><input type="number" id="neck" value="38" step="0.1" oninput="calcBF()"></div>
  <div class="input-group"><label>Waist Circumference (cm)</label><input type="number" id="waist" value="80" step="0.1" oninput="calcBF()"></div>
</div>
<div class="tool-row" id="hip-row" style="display:none">
  <div class="input-group" style="flex:1 1 100%"><label>Hip Circumference (cm)</label><input type="number" id="hip" value="95" step="0.1" oninput="calcBF()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Body Fat Percentage</div>
  <div class="value" id="result">15.2%</div>
  <div style="margin-top:8px;font-size:14px;color:var(--text-soft)">Category: <strong id="cat">Fitness</strong></div>
</div>
""",
    "js": """
function calcBF(){const g=document.getElementById('gender').value;const h=parseFloat(document.getElementById('height').value)||0;const n=parseFloat(document.getElementById('neck').value)||0;const w=parseFloat(document.getElementById('waist').value)||0;document.getElementById('hip-row').style.display=g==='female'?'flex':'none';let bf;if(g==='male'){bf=495/Math.PI*0.5*(w-n)*(w-n)/(h*h)-450+10}else{const hip=parseFloat(document.getElementById('hip').value)||0;bf=495/Math.PI*0.5*(w+hip-n)*(w+hip-n)/(h*h)-450+10}bf=Math.max(0,bf);document.getElementById('result').textContent=bf.toFixed(1)+'%';let cat='';if(g==='male'){if(bf<6)cat='Essential';else if(bf<14)cat='Fitness';else if(bf<18)cat='Average';else cat='High'}else{if(bf<14)cat='Essential';else if(bf<21)cat='Fitness';else if(bf<25)cat='Average';else cat='High'}document.getElementById('cat').textContent=cat}
calcBF();
"""
})

TOOLS.append({
    "filename": "water-intake-calculator.html",
    "title": "Water Intake Calculator",
    "desc": "Calculate recommended daily water intake based on weight and activity. Free online hydration calculator.",
    "category": "Health Calculators",
    "keywords": "water intake calculator, daily water needs, hydration calculator, how much water to drink, water requirement",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Weight (kg)</label><input type="number" id="weight" value="70" oninput="calcWater()"></div>
  <div class="input-group"><label>Exercise (minutes/day)</label><input type="number" id="exercise" value="30" oninput="calcWater()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Daily Water Intake</div>
  <div class="value" id="liters">2.65 liters</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Ounces: <strong id="oz">89.7</strong></span>
    <span>Glasses (250ml): <strong id="glasses">10.6</strong></span>
  </div>
</div>
""",
    "js": """
function calcWater(){const w=parseFloat(document.getElementById('weight').value)||0;const e=parseFloat(document.getElementById('exercise').value)||0;const ml=w*35+e*12;const l=ml/1000;document.getElementById('liters').textContent=l.toFixed(2)+' liters';document.getElementById('oz').textContent=(ml/29.574).toFixed(1);document.getElementById('glasses').textContent=(ml/250).toFixed(1)}
calcWater();
"""
})

TOOLS.append({
    "filename": "heart-rate-calculator.html",
    "title": "Heart Rate Calculator",
    "desc": "Calculate target heart rate zones for exercise. Free online heart rate zone calculator.",
    "category": "Health Calculators",
    "keywords": "heart rate calculator, target heart rate, heart rate zones, max heart rate, exercise heart rate",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Age</label><input type="number" id="age" value="25" oninput="calcHR()"></div>
  <div class="input-group"><label>Resting HR (bpm)</label><input type="number" id="rest" value="60" oninput="calcHR()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Heart Rate Zones</div>
  <div style="margin-top:8px">
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Max HR</span><strong id="max">195 bpm</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Zone 1 (50-60%)</span><strong id="z1">98-117 bpm</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Zone 2 (60-70%)</span><strong id="z2">117-137 bpm</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Zone 3 (70-80%)</span><strong id="z3">137-156 bpm</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Zone 4 (80-90%)</span><strong id="z4">156-176 bpm</strong></div>
    <div style="display:flex;justify-content:space-between;padding:4px 0"><span>Zone 5 (90-100%)</span><strong id="z5">176-195 bpm</strong></div>
  </div>
</div>
""",
    "js": """
function calcHR(){const a=parseInt(document.getElementById('age').value)||0;const max=220-a;document.getElementById('max').textContent=max+' bpm';document.getElementById('z1').textContent=Math.round(max*0.5)+'-'+Math.round(max*0.6)+' bpm';document.getElementById('z2').textContent=Math.round(max*0.6)+'-'+Math.round(max*0.7)+' bpm';document.getElementById('z3').textContent=Math.round(max*0.7)+'-'+Math.round(max*0.8)+' bpm';document.getElementById('z4').textContent=Math.round(max*0.8)+'-'+Math.round(max*0.9)+' bpm';document.getElementById('z5').textContent=Math.round(max*0.9)+'-'+max+' bpm'}
calcHR();
"""
})

# --- Text Tools ---

TOOLS.append({
    "filename": "find-and-replace.html",
    "title": "Find and Replace Text",
    "desc": "Find and replace text online. Free online text find and replace tool with case-sensitive and regex support.",
    "category": "Text Tools",
    "keywords": "find and replace, text replace, search and replace, replace text, online text editor",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Text</label><textarea id="input" placeholder="Enter your text here...">Hello World! Hello everyone!</textarea></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Find</label><input type="text" id="find" value="Hello" oninput="doReplace()"></div>
  <div class="input-group"><label>Replace With</label><input type="text" id="replace" value="Hi" oninput="doReplace()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Options</label><label style="font-size:14px;font-weight:normal"><input type="checkbox" id="ci" onchange="doReplace()"> Case insensitive</label></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Result</div>
  <textarea id="output" style="margin-top:8px;background:var(--card)" readonly>Hi World! Hi everyone!</textarea>
</div>
""",
    "js": """
function doReplace(){const t=document.getElementById('input').value;const f=document.getElementById('find').value;const r=document.getElementById('replace').value;const ci=document.getElementById('ci').checked;if(!f){document.getElementById('output').value=t;return}let result;if(ci){const re=new RegExp(f.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&'),'gi');result=t.replace(re,r)}else{result=t.split(f).join(r)}document.getElementById('output').value=result}
doReplace();
"""
})

TOOLS.append({
    "filename": "word-frequency-counter.html",
    "title": "Word Frequency Counter",
    "desc": "Count word frequency in text. Free online word frequency analyzer and text analysis tool.",
    "category": "Text Tools",
    "keywords": "word frequency counter, word frequency, text analysis, word count frequency, word occurrence",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Text</label><textarea id="input" placeholder="Enter text to analyze..." oninput="countFreq()">the quick brown fox jumps over the lazy dog the cat</textarea></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Word Frequency</div>
  <div id="output" style="margin-top:8px"></div>
</div>
""",
    "js": """
function countFreq(){const t=document.getElementById('input').value.toLowerCase();const words=t.match(/\\b\\w+\\b/g)||[];const freq={};for(const w of words){freq[w]=(freq[w]||0)+1}const sorted=Object.entries(freq).sort((a,b)=>b[1]-a[1]);let html='<table style="width:100%;border-collapse:collapse"><tr style="text-align:left;border-bottom:2px solid var(--border)"><th style="padding:4px 8px">Word</th><th style="padding:4px 8px">Count</th></tr>';for(const[w,c]of sorted.slice(0,50)){html+='<tr style="border-bottom:1px solid var(--border)"><td style="padding:4px 8px">'+w+'</td><td style="padding:4px 8px">'+c+'</td></tr>'}html+='</table>';document.getElementById('output').innerHTML=html}
countFreq();
"""
})

TOOLS.append({
    "filename": "markdown-to-html.html",
    "title": "Markdown to HTML Converter",
    "desc": "Convert Markdown text to HTML. Free online Markdown to HTML converter with live preview.",
    "category": "Text Tools",
    "keywords": "markdown to html, markdown converter, md to html, markdown preview, markdown editor",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Markdown Input</label><textarea id="input" placeholder="# Hello World&#10;&#10;This is **bold** and *italic*.&#10;&#10;- Item 1&#10;- Item 2" oninput="convert()"># Hello World

This is **bold** and *italic*.

- Item 1
- Item 2</textarea></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">HTML Output</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:13px;margin:0;color:var(--text)"></pre>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Preview</div>
  <div id="preview" style="padding:12px"></div>
</div>
""",
    "js": """
function convert(){let md=document.getElementById('input').value;let html=md;html=html.replace(/^### (.+)$/gm,'<h3>$1</h3>');html=html.replace(/^## (.+)$/gm,'<h2>$1</h2>');html=html.replace(/^# (.+)$/gm,'<h1>$1</h1>');html=html.replace(/\\*\\*(.+?)\\*\\*/g,'<strong>$1</strong>');html=html.replace(/\\*(.+?)\\*/g,'<em>$1</em>');html=html.replace(/^- (.+)$/gm,'<li>$1</li>');html=html.replace(/(<li>.*<\\/li>)/s,'<ul>$1</ul>');html=html.replace(/^(?!<[hul])(.+)/gm,'<p>$1</p>');document.getElementById('output').textContent=html;document.getElementById('preview').innerHTML=html}
convert();
"""
})

TOOLS.append({
    "filename": "csv-to-json.html",
    "title": "CSV to JSON Converter",
    "desc": "Convert CSV data to JSON format. Free online CSV to JSON converter.",
    "category": "Developer Tools",
    "keywords": "csv to json, csv converter, csv to json converter, convert csv, csv parser",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>CSV Input (first row = headers)</label><textarea id="input" placeholder="name,age,city&#10;John,30,New York&#10;Jane,25,London" oninput="convert()">name,age,city
John,30,New York
Jane,25,London</textarea></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">JSON Output</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:13px;margin:0;color:var(--text)"></pre>
</div>
""",
    "js": """
function convert(){const csv=document.getElementById('input').value.trim();if(!csv){document.getElementById('output').textContent='';return}const lines=csv.split('\\n');const headers=lines[0].split(',').map(h=>h.trim());const result=[];for(let i=1;i<lines.length;i++){const vals=lines[i].split(',');const obj={};for(let j=0;j<headers.length;j++){obj[headers[j]]=vals[j]?vals[j].trim():''}result.push(obj)}document.getElementById('output').textContent=JSON.stringify(result,null,2)}
convert();
"""
})

TOOLS.append({
    "filename": "json-to-csv.html",
    "title": "JSON to CSV Converter",
    "desc": "Convert JSON data to CSV format. Free online JSON to CSV converter.",
    "category": "Developer Tools",
    "keywords": "json to csv, json converter, json to csv converter, convert json to csv, json parser",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>JSON Input (array of objects)</label><textarea id="input" placeholder='[{"name":"John","age":30},{"name":"Jane","age":25}]' oninput="convert()">[{"name":"John","age":30},{"name":"Jane","age":25}]</textarea></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">CSV Output</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:13px;margin:0;color:var(--text)"></pre>
</div>
""",
    "js": """
function convert(){try{const data=JSON.parse(document.getElementById('input').value);if(!Array.isArray(data)||data.length===0){document.getElementById('output').textContent='Please enter a non-empty JSON array';return}const keys=Object.keys(data[0]);let csv=keys.join(',')+'\\n';for(const row of data){csv+=keys.map(k=>{const v=row[k]!==undefined?String(row[k]):'';return v.includes(',')?'"'+v+'"':v}).join(',')+'\\n'}document.getElementById('output').textContent=csv.trim()}catch(e){document.getElementById('output').textContent='Error: '+e.message}}
convert();
"""
})

# --- Color Tools ---

TOOLS.append({
    "filename": "color-picker.html",
    "title": "Color Picker",
    "desc": "Pick colors and get HEX, RGB and HSL values. Free online color picker tool.",
    "category": "Color Tools",
    "keywords": "color picker, color selector, pick color, hex color picker, rgb color picker",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Color Picker</label><input type="color" id="picker" value="#3366ff" oninput="updateColor()"></div>
  <div class="input-group"><label>HEX</label><input type="text" id="hex" value="#3366ff" oninput="fromHex()"></div>
</div>
<div style="display:flex;gap:16px;margin-top:16px;align-items:center">
  <div id="preview" style="width:120px;height:60px;border-radius:8px;border:2px solid var(--border);background:#3366ff"></div>
  <div style="flex:1">
    <div style="padding:4px 0">RGB: <strong id="rgb">51, 102, 255</strong></div>
    <div style="padding:4px 0">HSL: <strong id="hsl">225&deg;, 100%, 60%</strong></div>
    <div style="padding:4px 0">HEX: <strong id="hexval">#3366ff</strong></div>
  </div>
</div>
""",
    "js": """
function updateColor(){const hex=document.getElementById('picker').value;document.getElementById('hex').value=hex;displayColor(hex)}
function fromHex(){let h=document.getElementById('hex').value;if(!h.startsWith('#'))h='#'+h;if(/^#[0-9a-fA-F]{6}$/.test(h)){document.getElementById('picker').value=h;displayColor(h)}}
function displayColor(hex){const r=parseInt(hex.substr(1,2),16);const g=parseInt(hex.substr(3,2),16);const b=parseInt(hex.substr(5,2),16);document.getElementById('preview').style.background=hex;document.getElementById('hexval').textContent=hex.toUpperCase();document.getElementById('rgb').textContent=r+', '+g+', '+b;const r1=r/255,g1=g/255,b1=b/255;const max=Math.max(r1,g1,b1),min=Math.min(r1,g1,b1);let h,s,l=(max+min)/2;if(max===min){h=0;s=0}else{const d=max-min;s=l>0.5?d/(2-max-min):d/(max+min);switch(max){case r1:h=(g1-b1)/d+(g1<b1?6:0);break;case g1:h=(b1-r1)/d+2;break;case b1:h=(r1-g1)/d+4;break}h=h/6}document.getElementById('hsl').textContent=Math.round(h*360)+'\u00b0, '+Math.round(s*100)+'%, '+Math.round(l*100)+'%'}
updateColor();
"""
})

TOOLS.append({
    "filename": "hsl-to-hex.html",
    "title": "HSL to HEX Converter",
    "desc": "Convert HSL color values to HEX color code. Free online HSL to HEX converter.",
    "category": "Color Tools",
    "keywords": "hsl to hex, hsl converter, hsl to hex color, color converter, hsl to rgb",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Hue (0-360)</label><input type="number" id="h" value="225" min="0" max="360" oninput="convert()"></div>
  <div class="input-group"><label>Saturation (%)</label><input type="number" id="s" value="100" min="0" max="100" oninput="convert()"></div>
  <div class="input-group"><label>Lightness (%)</label><input type="number" id="l" value="60" min="0" max="100" oninput="convert()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">HEX Color</div>
  <div class="value" id="hex">#3366FF</div>
  <div style="display:flex;gap:16px;margin-top:8px;align-items:center">
    <div id="preview" style="width:80px;height:40px;border-radius:6px;background:#3366ff"></div>
    <span style="font-size:14px;color:var(--text-soft)">RGB: <strong id="rgb">51, 102, 255</strong></span>
  </div>
</div>
""",
    "js": """
function convert(){const h=parseFloat(document.getElementById('h').value)||0;const s=parseFloat(document.getElementById('s').value)/100||0;const l=parseFloat(document.getElementById('l').value)/100||0;const c=(1-Math.abs(2*l-1))*s;const x=c*(1-Math.abs((h/60)%2-1));const m=l-c/2;let r,g,b;if(h<60){r=c;g=x;b=0}else if(h<120){r=x;g=c;b=0}else if(h<180){r=0;g=c;b=x}else if(h<240){r=0;g=x;b=c}else if(h<300){r=x;g=0;b=c}else{r=c;g=0;b=x}r=Math.round((r+m)*255);g=Math.round((g+m)*255);b=Math.round((b+m)*255);const hex='#'+[r,g,b].map(v=>v.toString(16).padStart(2,'0')).join('').toUpperCase();document.getElementById('hex').textContent=hex;document.getElementById('rgb').textContent=r+', '+g+', '+b;document.getElementById('preview').style.background=hex}
convert();
"""
})

TOOLS.append({
    "filename": "hex-to-hsl.html",
    "title": "HEX to HSL Converter",
    "desc": "Convert HEX color code to HSL values. Free online HEX to HSL converter.",
    "category": "Color Tools",
    "keywords": "hex to hsl, hex converter, hex to hsl color, color converter, hex to hsl values",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>HEX Color</label><input type="text" id="hex" value="#3366ff" oninput="convert()" style="font-family:'Courier New',monospace"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">HSL Values</div>
  <div class="value" id="hsl">225&deg;, 100%, 60%</div>
  <div style="display:flex;gap:16px;margin-top:8px;align-items:center">
    <div id="preview" style="width:80px;height:40px;border-radius:6px;background:#3366ff"></div>
    <span style="font-size:14px;color:var(--text-soft)">RGB: <strong id="rgb">51, 102, 255</strong></span>
  </div>
</div>
""",
    "js": """
function convert(){let hex=document.getElementById('hex').value;if(!hex.startsWith('#'))hex='#'+hex;if(!/^#[0-9a-fA-F]{6}$/.test(hex))return;const r=parseInt(hex.substr(1,2),16)/255;const g=parseInt(hex.substr(3,2),16)/255;const b=parseInt(hex.substr(5,2),16)/255;const max=Math.max(r,g,b),min=Math.min(r,g,b);let h,s,l=(max+min)/2;if(max===min){h=0;s=0}else{const d=max-min;s=l>0.5?d/(2-max-min):d/(max+min);switch(max){case r:h=(g-b)/d+(g<b?6:0);break;case g:h=(b-r)/d+2;break;case b:h=(r-g)/d+4;break}h=h/6}document.getElementById('hsl').innerHTML=Math.round(h*360)+'&deg;, '+Math.round(s*100)+'%, '+Math.round(l*100)+'%';document.getElementById('rgb').textContent=Math.round(r*255)+', '+Math.round(g*255)+', '+Math.round(b*255);document.getElementById('preview').style.background=hex}
convert();
"""
})

# --- More Web/Dev Tools ---

TOOLS.append({
    "filename": "css-minifier.html",
    "title": "CSS Minifier",
    "desc": "Minify CSS code to reduce file size. Free online CSS minifier and compressor.",
    "category": "Developer Tools",
    "keywords": "css minifier, css compressor, minify css, css optimizer, css shrink",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>CSS Input</label><textarea id="input" placeholder="Paste CSS here..." style="min-height:120px">body {
  margin: 0;
  padding: 20px;
  background: #fff;
}</textarea></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="minifyCSS()">Minify</button><button class="btn btn-secondary" onclick="copyResult()">Copy</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Minified CSS</div>
  <textarea id="output" style="margin-top:8px" readonly></textarea>
  <div style="margin-top:4px;font-size:12px;color:var(--text-soft)">Original: <strong id="orig">0 bytes</strong> | Minified: <strong id="min">0 bytes</strong> | Saved: <strong id="saved">0%</strong></div>
</div>
""",
    "js": """
function minifyCSS(){let css=document.getElementById('input').value;const orig=css.length;css=css.replace(/\\/\\*[\\s\\S]*?\\*\\//g,'');css=css.replace(/\\s+/g,' ');css=css.replace(/\\s*([{}:;,])\\s*/g,'$1');css=css.replace(/;/}/g,'}');css=css.trim();document.getElementById('output').value=css;document.getElementById('orig').textContent=orig+' bytes';document.getElementById('min').textContent=css.length+' bytes';document.getElementById('saved').textContent=orig>0?Math.round((1-css.length/orig)*100)+'%':'0%'}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').value)}
minifyCSS();
"""
})

TOOLS.append({
    "filename": "js-minifier.html",
    "title": "JS Minifier",
    "desc": "Minify JavaScript code to reduce file size. Free online JavaScript minifier and compressor.",
    "category": "Developer Tools",
    "keywords": "js minifier, javascript minifier, minify js, js compressor, javascript compressor",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>JavaScript Input</label><textarea id="input" placeholder="Paste JS here..." style="min-height:120px">function hello(name) {
  console.log("Hello " + name);
}</textarea></div>
</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="minifyJS()">Minify</button><button class="btn btn-secondary" onclick="copyResult()">Copy</button></div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Minified JS</div>
  <textarea id="output" style="margin-top:8px" readonly></textarea>
  <div style="margin-top:4px;font-size:12px;color:var(--text-soft)">Original: <strong id="orig">0 bytes</strong> | Minified: <strong id="min">0 bytes</strong> | Saved: <strong id="saved">0%</strong></div>
</div>
""",
    "js": """
function minifyJS(){let js=document.getElementById('input').value;const orig=js.length;js=js.replace(/\\/\\*[\\s\\S]*?\\*\\//g,'');js=js.replace(/\\/\\/.*$/gm,'');js=js.replace(/\\n\\s*$/g,'\\n');js=js.replace(/\\s+/g,' ');js=js.replace(/\\s*([=+\\-*/{}();,:<>!?&|])\\s*/g,'$1');js=js.trim();document.getElementById('output').value=js;document.getElementById('orig').textContent=orig+' bytes';document.getElementById('min').textContent=js.length+' bytes';document.getElementById('saved').textContent=orig>0?Math.round((1-js.length/orig)*100)+'%':'0%'}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').value)}
minifyJS();
"""
})

TOOLS.append({
    "filename": "qr-code-generator.html",
    "title": "QR Code Generator",
    "desc": "Generate QR codes from any text or URL. Free online QR code generator.",
    "category": "Developer Tools",
    "keywords": "qr code generator, qr generator, create qr code, qr code maker, url to qr code",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Text or URL</label><input type="text" id="input" value="https://211014049.github.io/toolhub/" oninput="generateQR()"></div>
</div>
<div class="tool-row">
  <div class="input-group"><label>Size</label><select id="size" onchange="generateQR()"><option value="150">150px</option><option value="200" selected>200px</option><option value="300">300px</option><option value="400">400px</option></select></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px;text-align:center">
  <div class="label">QR Code</div>
  <div style="margin-top:12px;display:flex;justify-content:center">
    <img id="qrimg" src="" alt="QR Code" style="border:1px solid var(--border);border-radius:8px">
  </div>
</div>
""",
    "js": """
function generateQR(){const t=document.getElementById('input').value||' ';const s=document.getElementById('size').value;document.getElementById('qrimg').src='https://api.qrserver.com/v1/create-qr-code/?size='+s+'x'+s+'&data='+encodeURIComponent(t)}
generateQR();
"""
})

TOOLS.append({
    "filename": "image-to-base64.html",
    "title": "Image to Base64 Converter",
    "desc": "Convert images to Base64 encoded string. Free online image to Base64 converter.",
    "category": "Developer Tools",
    "keywords": "image to base64, base64 image converter, image encoder, base64 encode image, data uri",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Upload Image</label><input type="file" id="file" accept="image/*" onchange="convertImage()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Base64 Output</div>
  <textarea id="output" style="margin-top:8px;min-height:100px" readonly placeholder="Select an image to convert..."></textarea>
</div>
<div id="preview-box" style="margin-top:12px;text-align:center;display:none">
  <div class="label" style="margin-bottom:8px">Preview</div>
  <img id="preview" style="max-width:100%;max-height:200px;border-radius:8px;border:1px solid var(--border)">
</div>
""",
    "js": """
function convertImage(){const f=document.getElementById('file').files[0];if(!f)return;const r=new FileReader();r.onload=function(e){const b64=e.target.result;document.getElementById('output').value=b64;document.getElementById('preview').src=b64;document.getElementById('preview-box').style.display='block'};r.readAsDataURL(f)}
"""
})

# --- More Unit Converters ---

TOOLS.append({
    "filename": "mile-to-kilometer.html",
    "title": "Mile to Kilometer",
    "desc": "Convert miles to kilometers quickly and accurately. Free online mile to kilometer converter.",
    "category": "Length Converter",
    "keywords": "mile to kilometer, mile to km, convert miles, miles to kilometers, mile converter",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Miles</label><input type="number" id="input" value="5" oninput="convert()"></div>
  <div class="input-group"><label>Kilometers</label><input type="number" id="output" value="8.0467" oninput="convertRev()"></div>
</div>
<div class="info-section"><h2>How to Convert Miles to Kilometers</h2><p>1 mile = 1.609344 kilometers. To convert, multiply the number of miles by 1.609344.</p></div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('input').value)||0;document.getElementById('output').value=(v*1.609344).toFixed(6)}
function convertRev(){const v=parseFloat(document.getElementById('output').value)||0;document.getElementById('input').value=(v/1.609344).toFixed(6)}
convert();
"""
})

TOOLS.append({
    "filename": "ounce-to-gram.html",
    "title": "Ounce to Gram",
    "desc": "Convert ounces to grams quickly and accurately. Free online ounce to gram converter.",
    "category": "Weight Converter",
    "keywords": "ounce to gram, oz to g, convert ounces, ounces to grams, ounce converter",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Ounces (oz)</label><input type="number" id="input" value="8" oninput="convert()"></div>
  <div class="input-group"><label>Grams (g)</label><input type="number" id="output" value="226.796" oninput="convertRev()"></div>
</div>
<div class="info-section"><h2>How to Convert Ounces to Grams</h2><p>1 ounce = 28.3495 grams. To convert, multiply the number of ounces by 28.3495.</p></div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('input').value)||0;document.getElementById('output').value=(v*28.349523).toFixed(6)}
function convertRev(){const v=parseFloat(document.getElementById('output').value)||0;document.getElementById('input').value=(v/28.349523).toFixed(6)}
convert();
"""
})

TOOLS.append({
    "filename": "ounce-to-milliliter.html",
    "title": "Ounce to Milliliter",
    "desc": "Convert fluid ounces to milliliters. Free online fl oz to ml converter.",
    "category": "Volume Converter",
    "keywords": "ounce to milliliter, oz to ml, fl oz to ml, convert ounces, fluid ounce to ml",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Fluid Ounces (US)</label><input type="number" id="input" value="8" oninput="convert()"></div>
  <div class="input-group"><label>Milliliters</label><input type="number" id="output" value="236.588" oninput="convertRev()"></div>
</div>
<div class="info-section"><h2>How to Convert Fluid Ounces to Milliliters</h2><p>1 US fluid ounce = 29.5735 milliliters. To convert, multiply by 29.5735.</p></div>
""",
    "js": """
function convert(){const v=parseFloat(document.getElementById('input').value)||0;document.getElementById('output').value=(v*29.5735).toFixed(6)}
function convertRev(){const v=parseFloat(document.getElementById('output').value)||0;document.getElementById('input').value=(v/29.5735).toFixed(6)}
convert();
"""
})

# --- More Calculators ---

TOOLS.append({
    "filename": "lcm-calculator.html",
    "title": "LCM Calculator",
    "desc": "Find the Least Common Multiple of any set of numbers. Free online LCM calculator.",
    "category": "Math Calculators",
    "keywords": "lcm calculator, least common multiple, lcm finder, lcm of numbers, lowest common multiple",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Numbers (comma separated)</label><input type="text" id="nums" value="4, 6, 8" oninput="calcLCM()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Least Common Multiple</div>
  <div class="value" id="result">24</div>
</div>
""",
    "js": """
function gcd2(a,b){return b===0?a:gcd2(b,a%b)}
function calcLCM(){const nums=document.getElementById('nums').value.split(',').map(s=>parseInt(s.trim())).filter(n=>!isNaN(n)&&n>0);if(nums.length<1)return;let l=nums[0];for(let i=1;i<nums.length;i++)l=l*nums[i]/gcd2(l,nums[i]);document.getElementById('result').textContent=l}
calcLCM();
"""
})

TOOLS.append({
    "filename": "gcd-calculator.html",
    "title": "GCD Calculator",
    "desc": "Find the Greatest Common Divisor of any set of numbers. Free online GCD calculator.",
    "category": "Math Calculators",
    "keywords": "gcd calculator, greatest common divisor, gcd finder, gcd of numbers, highest common factor",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Numbers (comma separated)</label><input type="text" id="nums" value="48, 36, 24" oninput="calcGCD()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Greatest Common Divisor</div>
  <div class="value" id="result">12</div>
</div>
""",
    "js": """
function gcd2(a,b){return b===0?a:gcd2(b,a%b)}
function calcGCD(){const nums=document.getElementById('nums').value.split(',').map(s=>parseInt(s.trim())).filter(n=>!isNaN(n)&&n>0);if(nums.length<1)return;let g=nums[0];for(let i=1;i<nums.length;i++)g=gcd2(g,nums[i]);document.getElementById('result').textContent=g}
calcGCD();
"""
})

TOOLS.append({
    "filename": "square-root-calculator.html",
    "title": "Square Root Calculator",
    "desc": "Calculate the square root of any number. Free online square root calculator.",
    "category": "Math Calculators",
    "keywords": "square root calculator, sqrt calculator, root calculator, square root, math calculator",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%"><label>Number</label><input type="number" id="input" value="144" step="any" oninput="calcSQRT()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Square Root</div>
  <div class="value" id="result">12</div>
</div>
""",
    "js": """
function calcSQRT(){const v=parseFloat(document.getElementById('input').value)||0;if(v<0){document.getElementById('result').textContent='Cannot calculate square root of negative number';return}document.getElementById('result').textContent=Math.sqrt(v).toString()}
calcSQRT();
"""
})

TOOLS.append({
    "filename": "exponent-calculator.html",
    "title": "Exponent Calculator",
    "desc": "Calculate exponents and powers. Free online exponent calculator for any base and power.",
    "category": "Math Calculators",
    "keywords": "exponent calculator, power calculator, x to the power of y, exponential calculator, math power",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Base</label><input type="number" id="base" value="2" step="any" oninput="calcExp()"></div>
  <div class="input-group"><label>Exponent</label><input type="number" id="exp" value="10" step="any" oninput="calcExp()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Result</div>
  <div class="value" id="result">1,024</div>
</div>
""",
    "js": """
function calcExp(){const b=parseFloat(document.getElementById('base').value)||0;const e=parseFloat(document.getElementById('exp').value)||0;const r=Math.pow(b,e);document.getElementById('result').textContent=r.toLocaleString('en-US',{maximumFractionDigits:10})}
calcExp();
"""
})

TOOLS.append({
    "filename": "tip-calculator-2.html",
    "title": "Tip and Split Bill Calculator",
    "desc": "Calculate tip amount and split the bill among multiple people. Free online tip and bill splitter calculator.",
    "category": "Calculators",
    "keywords": "tip calculator, bill splitter, split the bill, tip amount, restaurant tip calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Bill Amount ($)</label><input type="number" id="bill" value="50" step="0.01" oninput="calcTip()"></div>
  <div class="input-group"><label>Tip (%)</label><input type="number" id="tip" value="15" step="1" oninput="calcTip()"></div>
  <div class="input-group"><label>Number of People</label><input type="number" id="people" value="2" min="1" oninput="calcTip()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Per Person</div>
  <div class="value" id="perperson">$28.75</div>
  <div style="display:flex;gap:24px;margin-top:8px;font-size:14px;color:var(--text-soft)">
    <span>Tip: <strong id="tipamt">$7.50</strong></span>
    <span>Total: <strong id="total">$57.50</strong></span>
  </div>
</div>
""",
    "js": """
function calcTip(){const b=parseFloat(document.getElementById('bill').value)||0;const t=parseFloat(document.getElementById('tip').value)||0;const p=parseInt(document.getElementById('people').value)||1;const tipAmt=b*t/100;const total=b+tipAmt;const per=total/p;document.getElementById('perperson').textContent='$'+per.toFixed(2);document.getElementById('tipamt').textContent='$'+tipAmt.toFixed(2);document.getElementById('total').textContent='$'+total.toFixed(2)}
calcTip();
"""
})

# Generate all pages
print(f"Generating {len(TOOLS)} new tool pages...")
for tool in TOOLS:
    related = [("percentage-calculator.html", "Percentage Calculator"), ("bmi-calculator.html", "BMI Calculator"), ("age-calculator.html", "Age Calculator"), ("tip-calculator.html", "Tip Calculator")]
    make_page(
        tool["filename"],
        tool["title"],
        tool["desc"],
        tool["category"],
        tool["keywords"],
        tool["html"],
        tool["js"],
        related
    )

print(f"\nDone! Generated {len(TOOLS)} new pages.")
print("\nNew files:")
for t in TOOLS:
    print(f"  {t['filename']} - {t['title']}")
