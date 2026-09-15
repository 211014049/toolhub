#!/usr/bin/env python3
"""ToolHub build script — generates a static multi-tool SEO website."""
import json, os, html, math, re
from datetime import datetime

OUT = os.path.join(os.path.dirname(__file__), "public")
SITE_URL = "https://toolhub.vercel.app"

# ============================================================
# UNIT CONVERTER DEFINITIONS
# ============================================================

CONVERTERS = {
    "length": {
        "title": "Length Converter",
        "desc": "Convert between meters, feet, inches, kilometers, miles and more.",
        "base": "Meter",
        "units": {
            "Meter (m)": 1, "Centimeter (cm)": 0.01, "Millimeter (mm)": 0.001,
            "Kilometer (km)": 1000, "Inch (in)": 0.0254, "Foot (ft)": 0.3048,
            "Yard (yd)": 0.9144, "Mile (mi)": 1609.344, "Nautical Mile": 1852,
        },
        "pairs": [
            ("Meter (m)", "Centimeter (cm)"), ("Meter (m)", "Foot (ft)"),
            ("Meter (m)", "Inch (in)"), ("Centimeter (cm)", "Inch (in)"),
            ("Kilometer (km)", "Mile (mi)"), ("Inch (in)", "Centimeter (cm)"),
            ("Foot (ft)", "Meter (m)"), ("Yard (yd)", "Meter (m)"),
            ("Centimeter (cm)", "Millimeter (mm)"), ("Meter (m)", "Yard (yd)"),
            ("Meter (m)", "Kilometer (km)"), ("Inch (in)", "Millimeter (mm)"),
        ]
    },
    "weight": {
        "title": "Weight Converter",
        "desc": "Convert between kilograms, pounds, ounces, grams, tons and more.",
        "base": "Kilogram",
        "units": {
            "Kilogram (kg)": 1, "Gram (g)": 0.001, "Milligram (mg)": 0.000001,
            "Metric Ton (t)": 1000, "Pound (lb)": 0.45359237, "Ounce (oz)": 0.028349523,
            "Stone": 6.35029,
        },
        "pairs": [
            ("Kilogram (kg)", "Pound (lb)"), ("Pound (lb)", "Kilogram (kg)"),
            ("Kilogram (kg)", "Gram (g)"), ("Gram (g)", "Ounce (oz)"),
            ("Kilogram (kg)", "Ounce (oz)"), ("Metric Ton (t)", "Kilogram (kg)"),
            ("Gram (g)", "Kilogram (kg)"), ("Pound (lb)", "Ounce (oz)"),
        ]
    },
    "temperature": {
        "title": "Temperature Converter",
        "desc": "Convert between Celsius, Fahrenheit and Kelvin.",
        "base": "Celsius",
        "units": {
            "Celsius (\u00b0C)": 1, "Fahrenheit (\u00b0F)": 1, "Kelvin (K)": 1,
        },
        "pairs": [
            ("Celsius (\u00b0C)", "Fahrenheit (\u00b0F)"), ("Fahrenheit (\u00b0F)", "Celsius (\u00b0C)"),
            ("Celsius (\u00b0C)", "Kelvin (K)"), ("Kelvin (K)", "Celsius (\u00b0C)"),
            ("Fahrenheit (\u00b0F)", "Kelvin (K)"), ("Kelvin (K)", "Fahrenheit (\u00b0F)"),
        ]
    },
    "volume": {
        "title": "Volume Converter",
        "desc": "Convert between liters, gallons, cups, milliliters and more.",
        "base": "Liter",
        "units": {
            "Liter (L)": 1, "Milliliter (mL)": 0.001, "Cubic Meter (m\u00b3)": 1000,
            "Gallon (US)": 3.78541, "Quart (US)": 0.946353, "Pint (US)": 0.473176,
            "Cup (US)": 0.236588, "Fluid Ounce (US)": 0.0295735,
        },
        "pairs": [
            ("Liter (L)", "Gallon (US)"), ("Gallon (US)", "Liter (L)"),
            ("Liter (L)", "Milliliter (mL)"), ("Milliliter (mL)", "Liter (L)"),
            ("Liter (L)", "Cup (US)"), ("Cup (US)", "Milliliter (mL)"),
            ("Gallon (US)", "Milliliter (mL)"), ("Fluid Ounce (US)", "Milliliter (mL)"),
        ]
    },
    "speed": {
        "title": "Speed Converter",
        "desc": "Convert between km/h, mph, m/s, knots and more.",
        "base": "Meter/second",
        "units": {
            "Meter/second (m/s)": 1, "Kilometer/hour (km/h)": 0.277778,
            "Mile/hour (mph)": 0.44704, "Knot": 0.514444, "Foot/second (ft/s)": 0.3048,
        },
        "pairs": [
            ("Kilometer/hour (km/h)", "Mile/hour (mph)"), ("Mile/hour (mph)", "Kilometer/hour (km/h)"),
            ("Meter/second (m/s)", "Kilometer/hour (km/h)"), ("Kilometer/hour (km/h)", "Meter/second (m/s)"),
            ("Knot", "Kilometer/hour (km/h)"), ("Knot", "Mile/hour (mph)"),
        ]
    },
    "data": {
        "title": "Data Size Converter",
        "desc": "Convert between bytes, KB, MB, GB, TB and PB.",
        "base": "Byte",
        "units": {
            "Byte (B)": 1, "Kilobyte (KB)": 1024, "Megabyte (MB)": 1048576,
            "Gigabyte (GB)": 1073741824, "Terabyte (TB)": 1099511627776,
            "Petabyte (PB)": 1125899906842624,
        },
        "pairs": [
            ("Megabyte (MB)", "Gigabyte (GB)"), ("Gigabyte (GB)", "Megabyte (MB)"),
            ("Kilobyte (KB)", "Megabyte (MB)"), ("Gigabyte (GB)", "Terabyte (TB)"),
            ("Terabyte (TB)", "Gigabyte (GB)"), ("Megabyte (MB)", "Kilobyte (KB)"),
            ("Byte (B)", "Kilobyte (KB)"), ("Kilobyte (KB)", "Byte (B)"),
        ]
    },
    "area": {
        "title": "Area Converter",
        "desc": "Convert between square meters, square feet, acres, hectares and more.",
        "base": "Square Meter",
        "units": {
            "Square Meter (m\u00b2)": 1, "Square Kilometer (km\u00b2)": 1000000,
            "Square Centimeter (cm\u00b2)": 0.0001, "Hectare": 10000,
            "Acre": 4046.86, "Square Foot (ft\u00b2)": 0.092903, "Square Inch (in\u00b2)": 0.00064516,
        },
        "pairs": [
            ("Square Meter (m\u00b2)", "Square Foot (ft\u00b2)"), ("Square Foot (ft\u00b2)", "Square Meter (m\u00b2)"),
            ("Acre", "Hectare"), ("Hectare", "Acre"),
            ("Square Foot (ft\u00b2)", "Square Inch (in\u00b2)"), ("Square Meter (m\u00b2)", "Acre"),
        ]
    },
    "time": {
        "title": "Time Converter",
        "desc": "Convert between seconds, minutes, hours, days, weeks, months and years.",
        "base": "Second",
        "units": {
            "Second (s)": 1, "Minute (min)": 60, "Hour (h)": 3600,
            "Day (d)": 86400, "Week": 604800, "Month": 2629746, "Year": 31556952,
        },
        "pairs": [
            ("Day (d)", "Hour (h)"), ("Hour (h)", "Minute (min)"), ("Minute (min)", "Second (s)"),
            ("Week", "Day (d)"), ("Month", "Day (d)"), ("Year", "Day (d)"),
            ("Hour (h)", "Second (s)"), ("Day (d)", "Minute (min)"),
        ]
    },
    "pressure": {
        "title": "Pressure Converter",
        "desc": "Convert between pascals, bar, psi, atm and mmHg.",
        "base": "Pascal",
        "units": {
            "Pascal (Pa)": 1, "Kilopascal (kPa)": 1000, "Bar": 100000,
            "Pound/square inch (psi)": 6894.76, "Atmosphere (atm)": 101325,
            "mmHg": 133.322,
        },
        "pairs": [
            ("Pound/square inch (psi)", "Bar"), ("Bar", "Pound/square inch (psi)"),
            ("Kilopascal (kPa)", "Pound/square inch (psi)"), ("Atmosphere (atm)", "Pound/square inch (psi)"),
        ]
    },
    "energy": {
        "title": "Energy Converter",
        "desc": "Convert between joules, calories, kilojoules, kilocalories and more.",
        "base": "Joule",
        "units": {
            "Joule (J)": 1, "Kilojoule (kJ)": 1000, "Calorie (cal)": 4.184,
            "Kilocalorie (kcal)": 4184, "Watt-hour (Wh)": 3600, "Kilowatt-hour (kWh)": 3600000,
        },
        "pairs": [
            ("Joule (J)", "Calorie (cal)"), ("Calorie (cal)", "Joule (J)"),
            ("Kilojoule (kJ)", "Kilocalorie (kcal)"), ("Kilocalorie (kcal)", "Kilojoule (kJ)"),
            ("Watt-hour (Wh)", "Kilowatt-hour (kWh)"), ("Kilowatt-hour (kWh)", "Watt-hour (Wh)"),
        ]
    },
}

# ============================================================
# UNIQUE TOOL DEFINITIONS
# ============================================================
# Each tool: slug, title, description, category, keywords,
# html_content (the tool UI), js (the tool logic)

UNIQUE_TOOLS = []

# --- Developer Tools ---

UNIQUE_TOOLS.append({
    "slug": "json-formatter",
    "title": "JSON Formatter & Validator",
    "desc": "Format, validate and beautify JSON data. Free online JSON formatter with syntax highlighting.",
    "category": "Developer Tools",
    "keywords": "json formatter, json validator, json beautifier, format json, pretty print json",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%">
    <label>Paste your JSON here</label>
    <textarea id="input" placeholder='{"name":"John","age":30,"city":"New York"}'></textarea>
  </div>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn" onclick="formatJSON()">Format</button>
  <button class="btn btn-secondary" onclick="minifyJSON()">Minify</button>
  <button class="btn btn-secondary" onclick="validateJSON()">Validate</button>
  <button class="btn btn-secondary" onclick="copyResult()">Copy Result</button>
  <button class="btn btn-secondary" onclick="clearAll()">Clear</button>
</div>
<div class="error-msg" id="error"></div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Formatted output</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0;color:var(--text)"></pre>
</div>
""",
    "js": """
function formatJSON(){
  try{
    const v=JSON.parse(document.getElementById('input').value);
    document.getElementById('output').textContent=JSON.stringify(v,null,2);
    document.getElementById('error').classList.remove('show');
  }catch(e){showErr(e.message)}
}
function minifyJSON(){
  try{
    const v=JSON.parse(document.getElementById('input').value);
    document.getElementById('output').textContent=JSON.stringify(v);
    document.getElementById('error').classList.remove('show');
  }catch(e){showErr(e.message)}
}
function validateJSON(){
  try{JSON.parse(document.getElementById('input').value);document.getElementById('error').classList.remove('show');document.getElementById('output').textContent='✓ Valid JSON';}catch(e){showErr(e.message)}
}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
function clearAll(){document.getElementById('input').value='';document.getElementById('output').textContent='';document.getElementById('error').classList.remove('show')}
function showErr(m){const e=document.getElementById('error');e.textContent='Error: '+m;e.classList.add('show')}
"""
})

UNIQUE_TOOLS.append({
    "slug": "base64-encoder",
    "title": "Base64 Encoder & Decoder",
    "desc": "Encode text to Base64 or decode Base64 to text. Free online Base64 converter.",
    "category": "Developer Tools",
    "keywords": "base64 encoder, base64 decoder, base64 converter, encode base64, decode base64",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%">
    <label>Input text</label>
    <textarea id="input" placeholder="Type text to encode or paste Base64 to decode..."></textarea>
  </div>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn" onclick="doEncode()">Encode</button>
  <button class="btn btn-secondary" onclick="doDecode()">Decode</button>
  <button class="btn btn-secondary" onclick="copyResult()">Copy</button>
  <button class="btn btn-secondary" onclick="document.getElementById('input').value='';document.getElementById('output').textContent=''">Clear</button>
</div>
<div class="error-msg" id="error"></div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Output</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0"></pre>
</div>
""",
    "js": """
function doEncode(){const t=document.getElementById('input').value;document.getElementById('output').textContent=btoa(unescape(encodeURIComponent(t)));document.getElementById('error').classList.remove('show')}
function doDecode(){try{const t=document.getElementById('input').value;document.getElementById('output').textContent=decodeURIComponent(escape(atob(t)));document.getElementById('error').classList.remove('show')}catch(e){const el=document.getElementById('error');el.textContent='Invalid Base64: '+e.message;el.classList.add('show')}}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "url-encoder",
    "title": "URL Encoder & Decoder",
    "desc": "Encode URL components or decode URL-encoded text. Free online URL encoder/decoder.",
    "category": "Developer Tools",
    "keywords": "url encoder, url decoder, percent encoding, uri encoder, uri decoder",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%">
    <label>Input</label>
    <textarea id="input" placeholder="Enter text or URL-encoded string..."></textarea>
  </div>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn" onclick="doEncode()">Encode</button>
  <button class="btn btn-secondary" onclick="doDecode()">Decode</button>
  <button class="btn btn-secondary" onclick="copyResult()">Copy</button>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Output</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0"></pre>
</div>
""",
    "js": """
function doEncode(){document.getElementById('output').textContent=encodeURIComponent(document.getElementById('input').value)}
function doDecode(){try{document.getElementById('output').textContent=decodeURIComponent(document.getElementById('input').value)}catch(e){document.getElementById('output').textContent='Error: '+e.message}}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "uuid-generator",
    "title": "UUID Generator",
    "desc": "Generate random UUIDs (v4). Create one or multiple UUIDs at once. Free online UUID generator.",
    "category": "Developer Tools",
    "keywords": "uuid generator, guid generator, random uuid, uuid v4, unique id generator",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 200px">
    <label>How many UUIDs?</label>
    <input type="number" id="count" value="1" min="1" max="100">
  </div>
  <div class="input-group" style="flex:0 0 auto;padding-top:28px">
    <button class="btn" onclick="genUUID()">Generate</button>
    <button class="btn btn-secondary" onclick="copyResult()">Copy All</button>
  </div>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Generated UUIDs</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0"></pre>
</div>
""",
    "js": """
function genUUID(){const n=Math.min(100,parseInt(document.getElementById('count').value)||1);const arr=[];for(let i=0;i<n;i++){arr.push(crypto.randomUUID())}document.getElementById('output').textContent=arr.join('\\n')}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "password-generator",
    "title": "Password Generator",
    "desc": "Generate strong, secure random passwords. Customize length and character sets. Free online password generator.",
    "category": "Developer Tools",
    "keywords": "password generator, random password, strong password generator, secure password",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:0 0 120px">
    <label>Length</label>
    <input type="number" id="length" value="16" min="4" max="64">
  </div>
  <div class="input-group" style="flex:0 0 auto;display:flex;flex-direction:column;gap:6px;padding-top:28px">
    <label style="display:flex;align-items:center;gap:6px;font-weight:400"><input type="checkbox" id="upper" checked> Uppercase (A-Z)</label>
    <label style="display:flex;align-items:center;gap:6px;font-weight:400"><input type="checkbox" id="lower" checked> Lowercase (a-z)</label>
    <label style="display:flex;align-items:center;gap:6px;font-weight:400"><input type="checkbox" id="nums" checked> Numbers (0-9)</label>
    <label style="display:flex;align-items:center;gap:6px;font-weight:400"><input type="checkbox" id="syms" checked> Symbols (!@#$)</label>
  </div>
</div>
<div style="margin-top:12px;display:flex;gap:8px">
  <button class="btn" onclick="genPwd()">Generate</button>
  <button class="btn btn-secondary" onclick="copyResult()">Copy</button>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Your password</div>
  <div id="output" style="font-family:'Courier New',monospace;font-size:1.2rem;word-break:break-all"></div>
</div>
""",
    "js": """
function genPwd(){const len=Math.min(64,Math.max(4,parseInt(document.getElementById('length').value)||16));let chars='';if(document.getElementById('upper').checked)chars+='ABCDEFGHIJKLMNOPQRSTUVWXYZ';if(document.getElementById('lower').checked)chars+='abcdefghijklmnopqrstuvwxyz';if(document.getElementById('nums').checked)chars+='0123456789';if(document.getElementById('syms').checked)chars+='!@#$%^&*()_+-=[]{}|;:,.<>?';if(!chars){document.getElementById('output').textContent='Select at least one option';return}let pwd='';const arr=new Uint32Array(len);crypto.getRandomValues(arr);for(let i=0;i<len;i++)pwd+=chars[arr[i]%chars.length];document.getElementById('output').textContent=pwd}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "hash-generator",
    "title": "MD5 & SHA Hash Generator",
    "desc": "Generate MD5 and SHA-256 hashes from text input. Free online hash generator.",
    "category": "Developer Tools",
    "keywords": "md5 hash generator, sha256 hash generator, hash calculator, online hash tool",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%">
    <label>Input text</label>
    <textarea id="input" placeholder="Enter text to hash..."></textarea>
  </div>
</div>
<button class="btn" style="margin-top:12px" onclick="genHash()">Generate Hashes</button>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">MD5 Hash</div>
  <div id="md5out" style="font-family:'Courier New',monospace;font-size:14px;word-break:break-all;margin-bottom:12px"></div>
  <div class="label">SHA-256 Hash</div>
  <div id="shaout" style="font-family:'Courier New',monospace;font-size:14px;word-break:break-all"></div>
</div>
""",
    "js": """
async function genHash(){
  const text=document.getElementById('input').value;
  // MD5 (simple implementation)
  document.getElementById('md5out').textContent=md5(text);
  // SHA-256
  const buf=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(text));
  const hash=Array.from(new Uint8Array(buf)).map(b=>b.toString(16).padStart(2,'0')).join('');
  document.getElementById('shaout').textContent=hash;
}
function md5(str){function r(n,r){var t=(65535&n)+(65535&r);return((n>>16)+(r>>16)+(t>>16))<<16|65535&t}function t(n,t){return n<<t|n>>>32-t}function e(n,e,o,u,c,f){return r(t(r(r(e,n),r(u,f)),c),o)}function o(n,t,o,u,c,f,i){return e(t&o|~t&u,n,t,c,f,i)}function u(n,t,o,u,c,f,i){return e(t&u|o&~u,n,t,c,f,i)}function c(n,t,o,u,c,f,i){return e(t^o^u,n,t,c,f,i)}function f(n,t,o,u,c,f,i){return e(o^(t|~u),n,t,c,f,i)}function i(n,t){var e,o,u,c,f;e=n[0],o=n[1],u=n[2],c=n[3],e=o(e,o,u,c,t[0],7,-680876936),u=o(u,c,e,o,t[1],12,-389564586),c=o(c,e,u,o,t[2],17,606105819),o=o(o,c,e,u,t[3],22,-1044525330),e=u(e,o,u,c,t[4],7,-176418897),u=o(u,c,e,o,t[5],12,1200080426),c=o(c,e,u,o,t[6],17,-1473231341),o=o(o,c,e,u,t[7],22,-45705983),e=u(e,o,u,c,t[8],7,1770035416),u=o(u,c,e,o,t[9],12,-1958414427),c=o(c,e,u,o,t[10],17,-42063),o=o(o,c,e,u,t[11],22,-1990404162),e=u(e,o,u,c,t[12],7,1804603682),u=o(u,c,e,o,t[13],12,-40341101),c=o(c,e,u,o,t[14],17,-1502002290),o=o(o,c,e,u,t[15],22,1236535329),e=c(e,o,u,c,t[1],5,-165796510),u=f(u,c,e,o,t[6],9,-1069501632),c=o(c,e,u,o,t[11],14,643717713),o=u(o,c,e,u,t[0],20,-373897744),e=c(e,o,u,c,t[5],5,-701558691),u=f(u,c,e,o,t[10],9,38016083),c=o(c,e,u,o,t[15],14,-660478335),o=u(o,c,e,u,t[4],20,-405537848),e=c(e,o,u,c,t[9],5,568446438),u=f(u,c,e,o,t[14],9,-1019803794),c=o(c,e,u,o,t[3],14,-187363961),o=u(o,c,e,u,t[8],20,1163531501),e=c(e,o,u,c,t[13],5,-1444681467),u=f(u,c,e,o,t[2],9,-51403784),c=o(c,e,u,o,t[7],14,1735328473),o=u(o,c,e,u,t[12],20,-1926607734),e=f(e,o,u,c,t[5],4,-378558),u=c(u,c,e,o,t[8],11,-2022574463),c=o(c,e,u,o,t[11],16,1839030562),o=u(o,c,e,u,t[14],23,-35309556),e=f(e,o,u,c,t[1],4,-1530992060),u=c(u,c,e,o,t[4],11,1272893353),c=o(c,e,u,o,t[7],16,-155497632),o=u(o,c,e,u,t[10],23,-1094730640),e=f(e,o,u,c,t[13],4,681279174),u=c(u,c,e,o,t[0],11,-358537222),c=o(c,e,u,o,t[3],16,-722521979),o=u(o,c,e,u,t[6],23,76029189),e=f(e,o,u,c,t[9],4,-640364487),u=c(u,c,e,o,t[12],11,-421815835),c=o(c,e,u,o,t[15],16,530742520),o=u(o,c,e,u,t[2],23,-995338651),e=c(e,o,u,c,t[0],6,-198630844),u=f(u,c,e,o,t[7],10,1126898140),c=o(c,e,u,o,t[14],15,-1416354905),o=u(o,c,e,u,t[5],21,-57434055),e=c(e,o,u,c,t[12],6,1700485571),u=f(u,c,e,o,t[3],10,-1894986606),c=o(c,e,u,o,t[10],15,-1051523),o=u(o,c,e,u,t[1],21,-2054922799),e=c(e,o,u,c,t[8],6,1873313359),u=f(u,c,e,o,t[15],10,-30611744),c=o(c,e,u,o,t[6],15,-1560198380),o=u(o,c,e,u,t[13],21,1309151649),e=c(e,o,u,c,t[4],6,-145523070),u=f(u,c,e,o,t[11],10,-1120210379),c=o(c,e,u,o,t[2],15,718787259),o=u(o,c,e,u,t[9],21,-343485551),n[0]=r(e,n[0]),n[1]=r(o,n[1]),n[2]=r(u,n[2]),n[3]=r(c,n[3])}function s(n,r){var t,e=(255&n.charCodeAt(r/8))<<r%8;return t=""+String.fromCharCode(e>>0&255)+String.fromCharCode(e>>8&255)+String.fromCharCode(e>>16&255)+String.fromCharCode(e>>24&255)}function a(n){var r,t=1+n.length,e=[],o=0;for(t+=-1==(3&n.length)?2:1-(3&t),r=0;r<n.length;r++)e[r>>2]|=(255&n.charCodeAt(r))<<r%4*8;e[e.length]=0,t=8*t,e[e.length-1]=t;var u=255&n.length;return e[e.length-2]|=u<<24,e[e.length-2]|=0,e}function d(n){var r,t="";for(r=0;r<32*r.length;r++)t+="0123456789abcdef".charAt(n[r>>2]>>r%4*8+4&15)+"0123456789abcdef".charAt(n[r>>2]>>r%4*8&15);return t}var n=function(n){var r=a(n);return function(n){var r=[1732584193,-271733879,-1732584194,271733878];!function(n,r){i(n,s(n,r))}(r,n.length),n[0]=0|r[0],n[1]=0|r[1],n[2]=-1&~r[2],n[3]=-1&~r[3]}(r),d(r)}(n)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "html-encoder",
    "title": "HTML Entity Encoder & Decoder",
    "desc": "Encode HTML entities or decode HTML-encoded text. Free online HTML encoder/decoder.",
    "category": "Developer Tools",
    "keywords": "html encoder, html decoder, html entities, encode html, html escape",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%">
    <label>Input</label>
    <textarea id="input" placeholder="Enter text or HTML-encoded string..."></textarea>
  </div>
</div>
<div style="display:flex;gap:8px;margin-top:12px">
  <button class="btn" onclick="doEncode()">Encode</button>
  <button class="btn btn-secondary" onclick="doDecode()">Decode</button>
  <button class="btn btn-secondary" onclick="copyResult()">Copy</button>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Output</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0"></pre>
</div>
""",
    "js": """
function doEncode(){const t=document.getElementById('input').value;const d=document.createElement('div');d.textContent=t;document.getElementById('output').textContent=d.innerHTML}
function doDecode(){const t=document.getElementById('input').value;const d=document.createElement('div');d.innerHTML=t;document.getElementById('output').textContent=d.textContent}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "regex-tester",
    "title": "Regex Tester & Matcher",
    "desc": "Test regular expressions against text. See matches highlighted. Free online regex tester.",
    "category": "Developer Tools",
    "keywords": "regex tester, regex matcher, regular expression tester, online regex tool",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:0 0 auto">
    <label>Pattern</label>
    <input type="text" id="pattern" placeholder="\\d+" style="font-family:'Courier New',monospace;min-width:300px">
  </div>
  <div class="input-group" style="flex:0 0 auto;padding-top:28px">
    <label style="display:flex;align-items:center;gap:6px;font-weight:400"><input type="checkbox" id="global" checked> Global (g)</label>
    <label style="display:flex;align-items:center;gap:6px;font-weight:400"><input type="checkbox" id="caseinsensitive"> Case-insensitive (i)</label>
  </div>
</div>
<div class="input-group" style="margin-top:12px">
  <label>Test string</label>
  <textarea id="teststr" placeholder="Enter text to test against..." style="min-height:120px"></textarea>
</div>
<button class="btn" style="margin-top:12px" onclick="testRegex()">Test</button>
<div class="error-msg" id="error"></div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Matches found: <span id="matchcount">0</span></div>
  <div id="output" style="margin-top:8px"></div>
</div>
""",
    "js": """
function testRegex(){
  const p=document.getElementById('pattern').value;
  const s=document.getElementById('teststr').value;
  let flags='';
  if(document.getElementById('global').checked)flags+='g';
  if(document.getElementById('caseinsensitive').checked)flags+='i';
  try{
    const re=new RegExp(p,flags);
    const matches=[];let m;
    if(flags.includes('g')){while((m=re.exec(s))!==null){matches.push(m[0]);if(m.index===re.lastIndex)re.lastIndex++}}
    else{m=re.exec(s);if(m)matches.push(m[0])}
    document.getElementById('matchcount').textContent=matches.length;
    document.getElementById('error').classList.remove('show');
    let html='';
    if(flags.includes('g')){let last=0;re.lastIndex=0;while((m=re.exec(s))!==null){html+=escapeHtml(s.substring(last,m.index))+'<mark style="background:var(--primary-light);color:var(--primary);padding:2px 4px;border-radius:3px">'+escapeHtml(m[0])+'</mark>';last=m.index+m[0].length;if(m.index===re.lastIndex)re.lastIndex++}html+=escapeHtml(s.substring(last))}else{m=re.exec(s);if(m){html=escapeHtml(s.substring(0,m.index))+'<mark style="background:var(--primary-light);color:var(--primary);padding:2px 4px;border-radius:3px">'+escapeHtml(m[0])+'</mark>'+escapeHtml(s.substring(m.index+m[0].length))}else{html=escapeHtml(s)}}
    document.getElementById('output').innerHTML=html;
  }catch(e){const el=document.getElementById('error');el.textContent='Invalid regex: '+e.message;el.classList.add('show')}
}
function escapeHtml(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
"""
})

UNIQUE_TOOLS.append({
    "slug": "jwt-decoder",
    "title": "JWT Decoder",
    "desc": "Decode JSON Web Tokens (JWT) and inspect header and payload. Free online JWT decoder.",
    "category": "Developer Tools",
    "keywords": "jwt decoder, jwt parser, json web token decoder, decode jwt, jwt debugger",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%">
    <label>Paste JWT token</label>
    <textarea id="input" placeholder="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." style="min-height:100px"></textarea>
  </div>
</div>
<button class="btn" style="margin-top:12px" onclick="decodeJWT()">Decode</button>
<div class="error-msg" id="error"></div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Header</div>
  <pre id="header" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0 0 12px"></pre>
  <div class="label">Payload</div>
  <pre id="payload" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0 0 12px"></pre>
  <div class="label">Signature</div>
  <pre id="sig" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0;color:var(--text-soft)"></pre>
</div>
""",
    "js": """
function decodeJWT(){
  const t=document.getElementById('input').value.trim();
  const parts=t.split('.');
  if(parts.length<2){const e=document.getElementById('error');e.textContent='Invalid JWT: expected 3 parts separated by dots';e.classList.add('show');return}
  document.getElementById('error').classList.remove('show');
  try{
    const dec=s=>decodeURIComponent(escape(atob(s.replace(/-/g,'+').replace(/_/g,'/'))));
    const h=JSON.parse(dec(parts[0]));
    const p=JSON.parse(dec(parts[1]));
    document.getElementById('header').textContent=JSON.stringify(h,null,2);
    document.getElementById('payload').textContent=JSON.stringify(p,null,2);
    document.getElementById('sig').textContent=parts[2]||'(none)';
  }catch(e){const el=document.getElementById('error');el.textContent='Error: '+e.message;el.classList.add('show')}
}
"""
})

UNIQUE_TOOLS.append({
    "slug": "cron-expression-parser",
    "title": "Cron Expression Parser",
    "desc": "Parse cron expressions and see the next execution times. Free online cron parser.",
    "category": "Developer Tools",
    "keywords": "cron parser, cron expression, crontab guru, cron schedule, next cron run",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:1 1 100%">
    <label>Cron expression</label>
    <input type="text" id="cron" placeholder="*/5 * * * *" style="font-family:'Courier New',monospace;font-size:16px">
  </div>
</div>
<button class="btn" style="margin-top:12px" onclick="parseCron()">Parse</button>
<div class="error-msg" id="error"></div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Next 5 execution times</div>
  <div id="output" style="margin-top:8px"></div>
</div>
""",
    "js": """
function parseCron(){
  const e=document.getElementById('cron').value.trim();
  const parts=e.split(/\\s+/);
  if(parts.length<5){document.getElementById('error').textContent='Invalid cron: need 5 fields';document.getElementById('error').classList.add('show');return}
  document.getElementById('error').classList.remove('show');
  const [m,h,dom,mon,dow]=parts.map(p=>parseField(p));
  const now=new Date();
  const times=[];
  const d=new Date(now.getTime());
  d.setSeconds(0);d.setMilliseconds(0);
  let count=0,safety=0;
  while(count<5&&safety<500000){safety++;d.setMinutes(d.getMinutes()+1);
    if(!matchField(m,d.getMinutes()))continue;
    if(!matchField(h,d.getHours()))continue;
    if(!matchField(dom,d.getDate()))continue;
    if(!matchField(mon,d.getMonth()+1))continue;
    if(!matchField(dow,d.getDay()))continue;
    times.push(new Date(d));
    count++;
  }
  document.getElementById('output').innerHTML=times.map(t=>'<div style="padding:4px 0">'+t.toLocaleString()+'</div>').join('')||'<div>No matches found</div>';
}
function parseField(f){if(f==='*')return null;if(f.startsWith('*/'))return{every:parseInt(f.slice(2))};if(f.includes(','))return{list:f.split(',').map(Number)};if(f.includes('-')){const p=f.split('-');return{range:[parseInt(p[0]),parseInt(p[1])]}};if(f.includes('/')){const p=f.split('/');return{start:parseInt(p[0]),every:parseInt(p[1])}};return{exact:parseInt(f)}}
function matchField(field,val){if(field===null)return true;if(field.exact!==undefined)return val===field.exact;if(field.every!==undefined)return val%field.every===0;if(field.list)return field.list.includes(val);if(field.range)return val>=field.range[0]&&val<=field.range[1];if(field.start!==undefined&&field.every!==undefined)return val>=field.start&&(val-field.start)%field.every===0;return true}
"""
})

# --- Text Tools ---

UNIQUE_TOOLS.append({
    "slug": "word-counter",
    "title": "Word Counter & Character Counter",
    "desc": "Count words, characters, sentences and paragraphs in text. Free online word count tool.",
    "category": "Text Tools",
    "keywords": "word counter, character counter, word count, letter count, text counter",
    "html": """
<div class="input-group">
  <label>Enter your text</label>
  <textarea id="input" placeholder="Paste or type your text here..." oninput="countStats()"></textarea>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:12px;margin-top:16px">
  <div class="result-box show" style="text-align:center;display:block"><div class="label">Words</div><div class="value" id="words">0</div></div>
  <div class="result-box show" style="text-align:center;display:block"><div class="label">Characters</div><div class="value" id="chars">0</div></div>
  <div class="result-box show" style="text-align:center;display:block"><div class="label">Sentences</div><div class="value" id="sentences">0</div></div>
  <div class="result-box show" style="text-align:center;display:block"><div class="label">Paragraphs</div><div class="value" id="paras">0</div></div>
  <div class="result-box show" style="text-align:center;display:block"><div class="label">Reading time</div><div class="value" id="rtime">0s</div></div>
</div>
""",
    "js": """
function countStats(){
  const t=document.getElementById('input').value;
  const words=t.trim()?t.trim().split(/\\s+/).length:0;
  const chars=t.length;
  const sentences=t.trim()?(t.match(/[.!?]+/g)||[]).length:0;
  const paras=t.trim()?t.split(/\\n\\s*\\n/).filter(p=>p.trim()).length:0;
  const rtime=Math.ceil(words/200*60);
  document.getElementById('words').textContent=words;
  document.getElementById('chars').textContent=chars;
  document.getElementById('sentences').textContent=sentences;
  document.getElementById('paras').textContent=paras;
  document.getElementById('rtime').textContent=rtime<60?rtime+'s':Math.floor(rtime/60)+'m '+(rtime%60)+'s';
}
"""
})

UNIQUE_TOOLS.append({
    "slug": "case-converter",
    "title": "Case Converter",
    "desc": "Convert text to uppercase, lowercase, title case, sentence case or camelCase. Free online case converter.",
    "category": "Text Tools",
    "keywords": "case converter, uppercase, lowercase, title case, camel case, text converter",
    "html": """
<div class="input-group">
  <label>Enter text</label>
  <textarea id="input" placeholder="Type or paste text here..."></textarea>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn btn-sm" onclick="conv('upper')">UPPERCASE</button>
  <button class="btn btn-sm" onclick="conv('lower')">lowercase</button>
  <button class="btn btn-sm" onclick="conv('title')">Title Case</button>
  <button class="btn btn-sm" onclick="conv('sentence')">Sentence case</button>
  <button class="btn btn-sm" onclick="conv('camel')">camelCase</button>
  <button class="btn btn-sm" onclick="conv('snake')">snake_case</button>
  <button class="btn btn-sm" onclick="conv('kebab')">kebab-case</button>
  <button class="btn btn-sm btn-secondary" onclick="copyResult()">Copy</button>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Result</div>
  <div id="output" style="word-break:break-all"></div>
</div>
""",
    "js": """
function conv(type){
  const t=document.getElementById('input').value;
  let r='';
  switch(type){
    case'upper':r=t.toUpperCase();break;
    case'lower':r=t.toLowerCase();break;
    case'title':r=t.replace(/\\w\\S*/g,w=>w.charAt(0).toUpperCase()+w.slice(1).toLowerCase());break;
    case'sentence':r=t.replace(/(^[a-z])|([.!?]\\s+[a-z])/g,c=>c.toUpperCase());break;
    case'camel':r=t.replace(/[^a-zA-Z0-9]+(.)/g,(_,c)=>c.toUpperCase()).replace(/^[A-Z]/,c=>c.toLowerCase());break;
    case'snake':r=t.toLowerCase().replace(/[^a-z0-9]+/g,'_').replace(/^_|_$/g,'');break;
    case'kebab':r=t.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');break;
  }
  document.getElementById('output').textContent=r;
}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "text-reverser",
    "title": "Text Reverser",
    "desc": "Reverse text characters, words or lines. Free online text reverser tool.",
    "category": "Text Tools",
    "keywords": "text reverser, reverse text, reverse string, flip text, backwards text",
    "html": """
<div class="input-group">
  <label>Enter text</label>
  <textarea id="input" placeholder="Type text to reverse..."></textarea>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn btn-sm" onclick="rev('chars')">Reverse Characters</button>
  <button class="btn btn-sm" onclick="rev('words')">Reverse Words</button>
  <button class="btn btn-sm" onclick="rev('lines')">Reverse Lines</button>
  <button class="btn btn-sm btn-secondary" onclick="copyResult()">Copy</button>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Result</div>
  <div id="output" style="word-break:break-all;white-space:pre-wrap"></div>
</div>
""",
    "js": """
function rev(type){
  const t=document.getElementById('input').value;
  let r='';
  if(type==='chars')r=t.split('').reverse().join('');
  else if(type==='words')r=t.split(/\\s+/).reverse().join(' ');
  else if(type==='lines')r=t.split('\\n').reverse().join('\\n');
  document.getElementById('output').textContent=r;
}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "lorem-ipsum-generator",
    "title": "Lorem Ipsum Generator",
    "desc": "Generate Lorem Ipsum placeholder text. Choose paragraphs, sentences or words. Free online Lorem Ipsum generator.",
    "category": "Text Tools",
    "keywords": "lorem ipsum, lorem ipsum generator, placeholder text, dummy text, filler text",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:0 0 120px">
    <label>Count</label>
    <input type="number" id="count" value="3" min="1" max="20">
  </div>
  <div class="input-group" style="flex:0 0 150px">
    <label>Type</label>
    <select id="type"><option value="paragraphs">Paragraphs</option><option value="sentences">Sentences</option><option value="words">Words</option></select>
  </div>
  <div class="input-group" style="flex:0 0 auto;padding-top:28px">
    <button class="btn" onclick="gen()">Generate</button>
    <button class="btn btn-secondary" onclick="copyResult()">Copy</button>
  </div>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Generated text</div>
  <div id="output" style="white-space:pre-wrap"></div>
</div>
""",
    "js": """
const W='lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate velit esse cillum eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum'.split(' ');
function gen(){
  const n=parseInt(document.getElementById('count').value)||3;
  const type=document.getElementById('type').value;
  let result=[];
  for(let i=0;i<n;i++){
    if(type==='paragraphs'){let p=[];let s=4+Math.floor(Math.random()*4);for(let j=0;j<s;j++){p.push(genSentence())}result.push(p.join(' '))}
    else if(type==='sentences')result.push(genSentence());
    else result.push(W[Math.floor(Math.random()*W.length)]);
  }
  document.getElementById('output').textContent=result.join(type==='paragraphs'?'\\n\\n':' ');
}
function genSentence(){let len=8+Math.floor(Math.random()*12);let words=[];for(let i=0;i<len;i++)words.push(W[Math.floor(Math.random()*W.length)]);let s=words.join(' ');return s.charAt(0).toUpperCase()+s.slice(1)+'.'}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "slug-generator",
    "title": "URL Slug Generator",
    "desc": "Convert text to URL-friendly slugs. Free online slug generator for SEO-friendly URLs.",
    "category": "Text Tools",
    "keywords": "slug generator, url slug, seo slug, permalink generator, url friendly text",
    "html": """
<div class="input-group">
  <label>Enter text</label>
  <textarea id="input" placeholder="Type a title to convert to slug..." oninput="genSlug()"></textarea>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">URL Slug</div>
  <div id="output" style="font-family:'Courier New',monospace;font-size:1.1rem;word-break:break-all"></div>
</div>
<button class="btn btn-sm btn-secondary" style="margin-top:8px" onclick="copyResult()">Copy</button>
""",
    "js": """
function genSlug(){
  const t=document.getElementById('input').value;
  const slug=t.toLowerCase().trim().replace(/[^a-z0-9\\s-]/g,'').replace(/[\\s_-]+/g,'-').replace(/^-+|-+$/g,'');
  document.getElementById('output').textContent=slug;
}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "remove-duplicate-lines",
    "title": "Remove Duplicate Lines",
    "desc": "Remove duplicate lines from text. Sort unique lines alphabetically. Free online duplicate line remover.",
    "category": "Text Tools",
    "keywords": "remove duplicate lines, deduplicate text, unique lines, remove duplicates",
    "html": """
<div class="input-group">
  <label>Paste text with duplicates</label>
  <textarea id="input" placeholder="One item per line..." style="min-height:160px"></textarea>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn btn-sm" onclick="rmDup(false)">Remove Duplicates</button>
  <button class="btn btn-sm" onclick="rmDup(true)">Remove & Sort</button>
  <button class="btn btn-sm btn-secondary" onclick="copyResult()">Copy</button>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Result (<span id="cnt">0</span> unique lines)</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0"></pre>
</div>
""",
    "js": """
function rmDup(sort){
  const lines=document.getElementById('input').value.split('\\n');
  const seen=new Set();const result=[];
  for(const l of lines){if(!seen.has(l)){seen.add(l);result.push(l)}}
  if(sort)result.sort();
  document.getElementById('output').textContent=result.join('\\n');
  document.getElementById('cnt').textContent=result.filter(l=>l.trim()).length;
}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

UNIQUE_TOOLS.append({
    "slug": "text-sorter",
    "title": "Text Line Sorter",
    "desc": "Sort text lines alphabetically, by length or reverse. Free online text sorter.",
    "category": "Text Tools",
    "keywords": "text sorter, sort lines, alphabetical sort, sort text, line sorter",
    "html": """
<div class="input-group">
  <label>Enter text (one item per line)</label>
  <textarea id="input" style="min-height:160px"></textarea>
</div>
<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
  <button class="btn btn-sm" onclick="sortText('az')">A → Z</button>
  <button class="btn btn-sm" onclick="sortText('za')">Z → A</button>
  <button class="btn btn-sm" onclick="sortText('len')">By Length</button>
  <button class="btn btn-sm" onclick="sortText('rev')">Reverse</button>
  <button class="btn btn-sm" onclick="sortText('shuffle')">Shuffle</button>
  <button class="btn btn-sm btn-secondary" onclick="copyResult()">Copy</button>
</div>
<div class="result-box" id="result" style="display:block;min-height:0;padding:16px">
  <div class="label">Result</div>
  <pre id="output" style="white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:14px;margin:0"></pre>
</div>
""",
    "js": """
function sortText(mode){
  let lines=document.getElementById('input').value.split('\\n');
  if(mode==='az')lines.sort();
  else if(mode==='za')lines.sort().reverse();
  else if(mode==='len')lines.sort((a,b)=>a.length-b.length);
  else if(mode==='rev')lines.reverse();
  else if(mode==='shuffle')lines=shuffle(lines);
  document.getElementById('output').textContent=lines.join('\\n');
}
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function copyResult(){navigator.clipboard.writeText(document.getElementById('output').textContent)}
"""
})

# --- Calculators ---

UNIQUE_TOOLS.append({
    "slug": "percentage-calculator",
    "title": "Percentage Calculator",
    "desc": "Calculate percentages, percentage change, and percentage of a number. Free online percentage calculator.",
    "category": "Calculators",
    "keywords": "percentage calculator, percent calculator, percentage of number, percentage change",
    "html": """
<div class="tool-card" style="margin-bottom:16px">
  <h3 style="font-size:1rem;margin-bottom:10px">What is X% of Y?</h3>
  <div class="tool-row">
    <div class="input-group"><label>Percentage (%)</label><input type="number" id="p1" value="20" oninput="calcP1()"></div>
    <div class="input-group"><label>Of number</label><input type="number" id="p2" value="150" oninput="calcP1()"></div>
  </div>
  <div class="result-box show" style="display:block;margin-top:12px"><div class="value" id="r1">30</div></div>
</div>
<div class="tool-card" style="margin-bottom:16px">
  <h3 style="font-size:1rem;margin-bottom:10px">X is what percent of Y?</h3>
  <div class="tool-row">
    <div class="input-group"><label>Number</label><input type="number" id="p3" value="30" oninput="calcP2()"></div>
    <div class="input-group"><label>Of total</label><input type="number" id="p4" value="150" oninput="calcP2()"></div>
  </div>
  <div class="result-box show" style="display:block;margin-top:12px"><div class="value" id="r2">20%</div></div>
</div>
<div class="tool-card">
  <h3 style="font-size:1rem;margin-bottom:10px">Percentage change from X to Y</h3>
  <div class="tool-row">
    <div class="input-group"><label>From</label><input type="number" id="p5" value="100" oninput="calcP3()"></div>
    <div class="input-group"><label>To</label><input type="number" id="p6" value="120" oninput="calcP3()"></div>
  </div>
  <div class="result-box show" style="display:block;margin-top:12px"><div class="value" id="r3">+20%</div></div>
</div>
""",
    "js": """
function calcP1(){const p=parseFloat(document.getElementById('p1').value)||0;const n=parseFloat(document.getElementById('p2').value)||0;document.getElementById('r1').textContent=(p/100*n).toLocaleString()}
function calcP2(){const a=parseFloat(document.getElementById('p3').value)||0;const b=parseFloat(document.getElementById('p4').value)||0;document.getElementById('r2').textContent=b?(a/b*100).toFixed(2)+'%':'—'}
function calcP3(){const a=parseFloat(document.getElementById('p5').value)||0;const b=parseFloat(document.getElementById('p6').value)||0;const c=a?((b-a)/a*100):0;document.getElementById('r3').textContent=(c>=0?'+':'')+c.toFixed(2)+'%'}
calcP1();calcP2();calcP3();
"""
})

UNIQUE_TOOLS.append({
    "slug": "bmi-calculator",
    "title": "BMI Calculator",
    "desc": "Calculate Body Mass Index (BMI) from height and weight. Free online BMI calculator with health categories.",
    "category": "Calculators",
    "keywords": "bmi calculator, body mass index, bmi chart, healthy weight calculator",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Height (cm)</label><input type="number" id="height" value="170" oninput="calcBMI()"></div>
  <div class="input-group"><label>Weight (kg)</label><input type="number" id="weight" value="65" oninput="calcBMI()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Your BMI</div>
  <div class="value" id="bmi">22.5</div>
  <div id="cat" style="font-size:14px;margin-top:4px;color:var(--text-soft)"></div>
</div>
""",
    "js": """
function calcBMI(){
  const h=parseFloat(document.getElementById('height').value)||0;
  const w=parseFloat(document.getElementById('weight').value)||0;
  if(h<=0||w<=0){document.getElementById('bmi').textContent='—';return}
  const bmi=w/((h/100)**2);
  document.getElementById('bmi').textContent=bmi.toFixed(1);
  let cat='';
  if(bmi<18.5)cat='Underweight';
  else if(bmi<25)cat='Normal weight';
  else if(bmi<30)cat='Overweight';
  else cat='Obese';
  document.getElementById('cat').textContent=cat;
}
calcBMI();
"""
})

UNIQUE_TOOLS.append({
    "slug": "age-calculator",
    "title": "Age Calculator",
    "desc": "Calculate exact age from date of birth. Years, months, days. Free online age calculator.",
    "category": "Calculators",
    "keywords": "age calculator, date of birth calculator, how old am i, age from birthday",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Date of birth</label><input type="date" id="dob" oninput="calcAge()"></div>
  <div class="input-group"><label>Age at date</label><input type="date" id="at" oninput="calcAge()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Your age</div>
  <div class="value" id="age">—</div>
  <div id="agedays" style="font-size:14px;margin-top:4px;color:var(--text-soft)"></div>
</div>
""",
    "js": """
function calcAge(){
  const dob=document.getElementById('dob').value;
  const at=document.getElementById('at').value||new Date().toISOString().slice(0,10);
  if(!dob){document.getElementById('age').textContent='—';return}
  const d1=new Date(dob),d2=new Date(at);
  if(d2<d1){document.getElementById('age').textContent='Invalid';return}
  let y=d2.getFullYear()-d1.getFullYear();
  let m=d2.getMonth()-d1.getMonth();
  let d=d2.getDate()-d1.getDate();
  if(d<0){m--;d+=new Date(d2.getFullYear(),d2.getMonth(),0).getDate()}
  if(m<0){y--;m+=12}
  document.getElementById('age').textContent=y+' years, '+m+' months, '+d+' days';
  const days=Math.floor((d2-d1)/(1000*60*60*24));
  document.getElementById('agedays').textContent=days.toLocaleString()+' days old';
}
document.getElementById('at').value=new Date().toISOString().slice(0,10);
"""
})

UNIQUE_TOOLS.append({
    "slug": "tip-calculator",
    "title": "Tip Calculator",
    "desc": "Calculate tip and split the bill. Free online tip calculator for restaurants.",
    "category": "Calculators",
    "keywords": "tip calculator, gratuity calculator, split bill, restaurant tip",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Bill amount ($)</label><input type="number" id="bill" value="50" oninput="calcTip()"></div>
  <div class="input-group"><label>Tip (%)</label><input type="number" id="tip" value="15" oninput="calcTip()"></div>
  <div class="input-group"><label>Split between</label><input type="number" id="split" value="1" min="1" oninput="calcTip()"></div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px;margin-top:16px">
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Tip</div><div class="value" id="tipamt">$7.50</div></div>
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Total</div><div class="value" id="total">$57.50</div></div>
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Per person</div><div class="value" id="per">$57.50</div></div>
</div>
""",
    "js": """
function calcTip(){
  const b=parseFloat(document.getElementById('bill').value)||0;
  const t=parseFloat(document.getElementById('tip').value)||0;
  const s=Math.max(1,parseInt(document.getElementById('split').value)||1);
  const tip=b*t/100;
  const total=b+tip;
  document.getElementById('tipamt').textContent='$'+tip.toFixed(2);
  document.getElementById('total').textContent='$'+total.toFixed(2);
  document.getElementById('per').textContent='$'+(total/s).toFixed(2);
}
calcTip();
"""
})

UNIQUE_TOOLS.append({
    "slug": "discount-calculator",
    "title": "Discount Calculator",
    "desc": "Calculate sale price after discount. See how much you save. Free online discount calculator.",
    "category": "Calculators",
    "keywords": "discount calculator, sale price calculator, percent off calculator, discount price",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Original price ($)</label><input type="number" id="price" value="100" oninput="calcDisc()"></div>
  <div class="input-group"><label>Discount (%)</label><input type="number" id="disc" value="20" oninput="calcDisc()"></div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px;margin-top:16px">
  <div class="result-box show" style="display:block;text-align:center"><div class="label">You save</div><div class="value" id="save">$20.00</div></div>
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Sale price</div><div class="value" id="sale">$80.00</div></div>
</div>
""",
    "js": """
function calcDisc(){
  const p=parseFloat(document.getElementById('price').value)||0;
  const d=parseFloat(document.getElementById('disc').value)||0;
  const save=p*d/100;
  document.getElementById('save').textContent='$'+save.toFixed(2);
  document.getElementById('sale').textContent='$'+(p-save).toFixed(2);
}
calcDisc();
"""
})

UNIQUE_TOOLS.append({
    "slug": "compound-interest-calculator",
    "title": "Compound Interest Calculator",
    "desc": "Calculate compound interest on investments. See growth over time. Free online compound interest calculator.",
    "category": "Calculators",
    "keywords": "compound interest calculator, investment calculator, interest calculator, savings growth",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>Principal ($)</label><input type="number" id="principal" value="10000" oninput="calcCI()"></div>
  <div class="input-group"><label>Annual rate (%)</label><input type="number" id="rate" value="7" step="0.1" oninput="calcCI()"></div>
  <div class="input-group"><label>Years</label><input type="number" id="years" value="10" oninput="calcCI()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">Final amount</div>
  <div class="value" id="amount">$19,671.51</div>
  <div id="interest" style="font-size:14px;margin-top:4px;color:var(--text-soft)"></div>
</div>
""",
    "js": """
function calcCI(){
  const p=parseFloat(document.getElementById('principal').value)||0;
  const r=(parseFloat(document.getElementById('rate').value)||0)/100;
  const y=parseInt(document.getElementById('years').value)||0;
  const amount=p*Math.pow(1+r,y);
  document.getElementById('amount').textContent='$'+amount.toLocaleString('en-US',{maximumFractionDigits:2,minimumFractionDigits:2});
  document.getElementById('interest').textContent='Total interest earned: $'+(amount-p).toLocaleString('en-US',{maximumFractionDigits:2,minimumFractionDigits:2});
}
calcCI();
"""
})

UNIQUE_TOOLS.append({
    "slug": "average-calculator",
    "title": "Average Calculator",
    "desc": "Calculate average (mean), median, mode and sum of numbers. Free online statistics calculator.",
    "category": "Calculators",
    "keywords": "average calculator, mean calculator, median calculator, mode calculator, statistics",
    "html": """
<div class="input-group">
  <label>Enter numbers (comma or space separated)</label>
  <textarea id="input" placeholder="10, 20, 30, 40, 50" oninput="calcAvg()" style="min-height:80px"></textarea>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:12px;margin-top:16px">
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Count</div><div class="value" id="cnt">0</div></div>
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Sum</div><div class="value" id="sum">0</div></div>
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Average</div><div class="value" id="avg">0</div></div>
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Median</div><div class="value" id="med">0</div></div>
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Min</div><div class="value" id="min">0</div></div>
  <div class="result-box show" style="display:block;text-align:center"><div class="label">Max</div><div class="value" id="max">0</div></div>
</div>
""",
    "js": """
function calcAvg(){
  const nums=document.getElementById('input').value.split(/[,\\s]+/).map(Number).filter(n=>!isNaN(n));
  if(nums.length===0){['cnt','sum','avg','med','min','max'].forEach(id=>document.getElementById(id).textContent='0');return}
  const sum=nums.reduce((a,b)=>a+b,0);
  const sorted=[...nums].sort((a,b)=>a-b);
  const med=sorted.length%2?sorted[Math.floor(sorted.length/2)]:(sorted[sorted.length/2-1]+sorted[sorted.length/2])/2;
  document.getElementById('cnt').textContent=nums.length;
  document.getElementById('sum').textContent=sum.toLocaleString();
  document.getElementById('avg').textContent=(sum/nums.length).toLocaleString('en-US',{maximumFractionDigits:4});
  document.getElementById('med').textContent=med.toLocaleString();
  document.getElementById('min').textContent=Math.min(...nums).toLocaleString();
  document.getElementById('max').textContent=Math.max(...nums).toLocaleString();
}
"""
})

# --- Color Tools ---

UNIQUE_TOOLS.append({
    "slug": "hex-to-rgb",
    "title": "HEX to RGB Converter",
    "desc": "Convert HEX color codes to RGB format. Free online color converter.",
    "category": "Color Tools",
    "keywords": "hex to rgb, color converter, hex color, rgb color, color code converter",
    "html": """
<div class="tool-row">
  <div class="input-group" style="flex:0 0 200px">
    <label>HEX color</label>
    <input type="text" id="hex" value="#4f46e5" oninput="hex2rgb()" style="font-family:'Courier New',monospace">
  </div>
  <div class="input-group" style="flex:0 0 60px;padding-top:28px">
    <input type="color" id="picker" value="#4f46e5" oninput="document.getElementById('hex').value=this.value;hex2rgb()" style="width:50px;height:40px;padding:0;border:none;border-radius:8px;cursor:pointer;background:none">
  </div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">RGB</div>
  <div class="value" id="rgb">rgb(79, 70, 229)</div>
  <div class="label" style="margin-top:8px">HSL</div>
  <div class="value" id="hsl" style="font-size:1rem;color:var(--text)">hsl(244, 76%, 59%)</div>
</div>
""",
    "js": """
function hex2rgb(){
  let h=document.getElementById('hex').value.replace('#','');
  if(h.length===3)h=h.split('').map(c=>c+c).join('');
  if(!/^[0-9a-fA-F]{6}$/.test(h)){document.getElementById('rgb').textContent='Invalid';return}
  const r=parseInt(h.slice(0,2),16),g=parseInt(h.slice(2,4),16),b=parseInt(h.slice(4,6),16);
  document.getElementById('rgb').textContent=`rgb(${r}, ${g}, ${b})`;
  const rmax=Math.max(r,g,b)/255,rmin=Math.min(r,g,b)/255;
  const l=(rmax+rmin)/2;
  let s=0,hd=0;
  if(rmax!==rmin){const d=rmax-rmin;s=l>0.5?d/(2-rmax-rmin):d/(rmax+rmin);
    if(r===rmax/255)hd=((g/255-rmin/255)/d+(rmax===r/255?0:6));
    else if(g/255===rmax)hd=(rmin/255-r/255)/d+2;
    else hd=(r/255-g/255)/d+4;hd*=60}
  document.getElementById('hsl').textContent=`hsl(${Math.round(hd)}, ${Math.round(s*100)}%, ${Math.round(l*100)}%)`;
  document.getElementById('picker').value='#'+h;
}
hex2rgb();
"""
})

UNIQUE_TOOLS.append({
    "slug": "rgb-to-hex",
    "title": "RGB to HEX Converter",
    "desc": "Convert RGB color values to HEX color codes. Free online color converter.",
    "category": "Color Tools",
    "keywords": "rgb to hex, color converter, rgb to hex code, color format converter",
    "html": """
<div class="tool-row">
  <div class="input-group"><label>R (0-255)</label><input type="number" id="r" value="79" min="0" max="255" oninput="rgb2hex()"></div>
  <div class="input-group"><label>G (0-255)</label><input type="number" id="g" value="70" min="0" max="255" oninput="rgb2hex()"></div>
  <div class="input-group"><label>B (0-255)</label><input type="number" id="b" value="229" min="0" max="255" oninput="rgb2hex()"></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">HEX</div>
  <div class="value" id="hex">#4f46e5</div>
  <div style="margin-top:8px;height:60px;border-radius:8px;background:#4f46e5" id="preview"></div>
</div>
""",
    "js": """
function rgb2hex(){
  const r=Math.min(255,Math.max(0,parseInt(document.getElementById('r').value)||0));
  const g=Math.min(255,Math.max(0,parseInt(document.getElementById('g').value)||0));
  const b=Math.min(255,Math.max(0,parseInt(document.getElementById('b').value)||0));
  const h='#'+[r,g,b].map(v=>v.toString(16).padStart(2,'0')).join('');
  document.getElementById('hex').textContent=h;
  document.getElementById('preview').style.background=h;
}
rgb2hex();
"""
})

UNIQUE_TOOLS.append({
    "slug": "gradient-generator",
    "title": "CSS Gradient Generator",
    "desc": "Create beautiful CSS gradients. Copy gradient CSS code. Free online gradient generator.",
    "category": "Color Tools",
    "keywords": "gradient generator, css gradient, color gradient, gradient maker, linear gradient",
    "html": """
<div style="height:120px;border-radius:12px;margin-bottom:16px" id="preview"></div>
<div class="tool-row">
  <div class="input-group" style="flex:0 0 80px"><label>Color 1</label><input type="color" id="c1" value="#4f46e5" oninput="genGrad()" style="width:60px;height:40px;padding:0;border:none;border-radius:8px;cursor:pointer;background:none"></div>
  <div class="input-group" style="flex:0 0 80px"><label>Color 2</label><input type="color" id="c2" value="#10b981" oninput="genGrad()" style="width:60px;height:40px;padding:0;border:none;border-radius:8px;cursor:pointer;background:none"></div>
  <div class="input-group" style="flex:0 0 120px"><label>Angle</label><input type="range" id="angle" value="90" min="0" max="360" oninput="genGrad()" style="padding-top:12px"></div>
  <div class="input-group" style="flex:0 0 120px"><label>Type</label><select id="type" onchange="genGrad()"><option value="linear">Linear</option><option value="radial">Radial</option></select></div>
</div>
<div class="result-box show" style="display:block;margin-top:16px">
  <div class="label">CSS Code</div>
  <pre id="code" style="font-family:'Courier New',monospace;font-size:14px;word-break:break-all;white-space:pre-wrap;margin:0"></pre>
</div>
<button class="btn btn-sm btn-secondary" style="margin-top:8px" onclick="copyCode()">Copy CSS</button>
""",
    "js": """
function genGrad(){
  const c1=document.getElementById('c1').value;
  const c2=document.getElementById('c2').value;
  const a=document.getElementById('angle').value;
  const t=document.getElementById('type').value;
  const css=t==='linear'?`linear-gradient(${a}deg, ${c1}, ${c2})`:`radial-gradient(circle, ${c1}, ${c2})`;
  document.getElementById('preview').style.background=css;
  document.getElementById('code').textContent='background: '+css+';';
}
function copyCode(){navigator.clipboard.writeText(document.getElementById('code').textContent)}
genGrad();
"""
})

# ============================================================
# HTML PAGE TEMPLATE
# ============================================================

def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def unit_short(unit):
    """Get the short form from 'Meter (m)' -> 'm', or 'Kilometer (km)' -> 'km'"""
    m = re.search(r'\(([^)]+)\)$', unit)
    return m.group(1) if m else unit

def unit_full(unit):
    """Get the full name from 'Meter (m)' -> 'Meter'"""
    return re.sub(r'\s*\([^)]+\)$', '', unit)

def make_page(title, desc, slug, category, keywords, breadcrumb, tool_html, tool_js, info_html, related, all_tools_js):
    """Generate a full HTML page for a tool."""
    url = f"{SITE_URL}/{slug}.html"
    jsonld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": title,
        "applicationCategory": category,
        "operatingSystem": "Any (web browser)",
        "description": desc,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "url": url
    }
    jsonld_str = json.dumps(jsonld, ensure_ascii=False)
    related_html = ""
    if related:
        related_html = f"""<div class="related"><h2>Related Tools</h2><div class="related-grid">{''.join(f'<a href="{r["url"]}">{r["title"]}</a>' for r in related)}</div></div>"""
    return f"""<!DOCTYPE html>
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
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="/static/style.css">
<script type="application/ld+json">{jsonld_str}</script>
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
  <div class="breadcrumb"><a href="/">Home</a> <span class="sep">›</span> <a href="/#category-{slugify(category)}">{category}</a> <span class="sep">›</span> {title}</div>
  <h1>{title}</h1>
  <p class="subtitle">{desc}</p>
  <div class="ad-slot"></div>
  <div class="tool-card">
    {tool_html}
  </div>
  <div class="info-section">
    {info_html}
  </div>
  {related_html}
  <div class="ad-slot"></div>
</div>
<footer>
  <p>ToolHub &mdash; Free Online Tools | <a href="/">All Tools</a></p>
  <p>&copy; 2026 ToolHub. All tools run in your browser. No data sent to servers.</p>
</footer>
<script src="/static/app.js"></script>
<script>window.ALL_TOOLS = {all_tools_js};</script>
<script>{tool_js}</script>
</body>
</html>"""

# ============================================================
# CONVERTER PAGE GENERATION
# ============================================================

def make_converter_pair_page(cat_key, cat, from_unit, to_unit, all_tools_js):
    from_name = unit_full(from_unit)
    to_name = unit_full(to_unit)
    from_short = unit_short(from_unit)
    to_short = unit_short(to_unit)
    slug = f"{slugify(from_name)}-to-{slugify(to_name)}"
    title = f"{from_name} to {to_name} Converter"
    desc = f"Convert {from_name.lower()} to {to_name.lower()} instantly. Free online {from_name} to {to_name} conversion tool. Accurate and fast."

    # Determine if temperature
    is_temp = cat_key == "temperature"

    if is_temp:
        # Special JS for temperature
        from_c = "Celsius" in from_name
        from_f = "Fahrenheit" in from_name
        from_k = "Kelvin" in from_name
        to_c = "Celsius" in to_name
        to_f = "Fahrenheit" in to_name
        to_k = "Kelvin" in to_name

        # Build conversion function
        if from_c and to_f:
            formula = "v*9/5+32"
        elif from_c and to_k:
            formula = "v+273.15"
        elif from_f and to_c:
            formula = "(v-32)*5/9"
        elif from_f and to_k:
            formula = "(v-32)*5/9+273.15"
        elif from_k and to_c:
            formula = "v-273.15"
        elif from_k and to_f:
            formula = "(v-273.15)*9/5+32"
        else:
            formula = "v"

        tool_js = f"""
function convert(){{
  const v=parseFloat(document.getElementById('input').value);
  if(isNaN(v)){{document.getElementById('error').classList.add('show');document.getElementById('result').classList.remove('show');return}}
  document.getElementById('error').classList.remove('show');
  const r={formula};
  document.getElementById('result-value').textContent=r.toLocaleString('en-US',{{maximumFractionDigits:6}});
  document.getElementById('result').classList.add('show');
}}
document.getElementById('input').addEventListener('input',convert);
"""
    else:
        from_factor = cat["units"][from_unit]
        to_factor = cat["units"][to_unit]
        tool_js = f"""
function convert(){{
  const v=parseFloat(document.getElementById('input').value);
  if(isNaN(v)){{document.getElementById('error').classList.add('show');document.getElementById('result').classList.remove('show');return}}
  document.getElementById('error').classList.remove('show');
  const r=v*{from_factor}/{to_factor};
  document.getElementById('result-value').textContent=r.toLocaleString('en-US',{{maximumFractionDigits:10}});
  document.getElementById('result').classList.add('show');
}}
document.getElementById('input').addEventListener('input',convert);
"""

    tool_html = f"""
<div class="tool-row">
  <div class="input-group" style="flex:1;min-width:200px">
    <label>{from_name}</label>
    <input type="number" id="input" placeholder="Enter value..." step="any" autofocus>
  </div>
  <div class="arrow">→</div>
  <div class="input-group" style="flex:1;min-width:200px">
    <label>{to_name}</label>
    <input type="text" id="output-display" readonly style="font-weight:600;font-size:1.2rem">
  </div>
</div>
<div class="error-msg" id="error">Please enter a valid number</div>
<div class="result-box" id="result">
  <div class="label">Result</div>
  <div class="value" id="result-value"></div>
</div>
"""
    # Update JS to also write to the output display field
    tool_js = tool_js.replace(
        "document.getElementById('result').classList.add('show');",
        "document.getElementById('result').classList.add('show');document.getElementById('output-display').value=r.toLocaleString('en-US',{maximumFractionDigits:10});"
    )

    # SEO info content
    info_html = f"""
<h2>How to convert {from_name} to {to_name}</h2>
<p>Use the calculator above to convert any value from {from_name.lower()} to {to_name.lower()}. Simply enter a number and the conversion happens instantly in your browser.</p>
<h2>Common {from_name} to {to_name} conversions</h2>
<ul>""" + "".join(f"<li>{v} {from_short} = {(v * from_factor / to_factor if not is_temp else eval_temp(from_name, to_name, v)) if not is_temp else eval_temp(from_name, to_name, v):.4g} {to_short}</li>" for v in [1, 5, 10, 20, 50, 100]) + f"""</ul>
<p>All conversions are calculated in your browser. No data is sent to any server.</p>
"""

    # Related tools: other pairs in same category
    related = []
    for (f, t) in cat["pairs"]:
        if f != from_unit or t != to_unit:
            r_slug = f"{slugify(unit_full(f))}-to-{slugify(unit_full(t))}.html"
            related.append({"url": r_slug, "title": f"{unit_full(f)} to {unit_full(t)}"})
        if len(related) >= 8:
            break

    return make_page(title, desc, slug, cat["title"], f"{from_name} to {to_name}, convert {from_name.lower()}, {from_short} to {to_short}", cat["title"], tool_html, tool_js, info_html, related, all_tools_js)

def eval_temp(from_name, to_name, v):
    if "Celsius" in from_name and "Fahrenheit" in to_name:
        return v * 9/5 + 32
    elif "Celsius" in from_name and "Kelvin" in to_name:
        return v + 273.15
    elif "Fahrenheit" in from_name and "Celsius" in to_name:
        return (v - 32) * 5/9
    elif "Fahrenheit" in from_name and "Kelvin" in to_name:
        return (v - 32) * 5/9 + 273.15
    elif "Kelvin" in from_name and "Celsius" in to_name:
        return v - 273.15
    elif "Kelvin" in from_name and "Fahrenheit" in to_name:
        return (v - 273.15) * 9/5 + 32
    return v

def make_converter_category_page(cat_key, cat, all_tools_js):
    slug = f"{slugify(cat['title'])}"
    title = cat["title"]
    desc = cat["desc"]

    units_js = json.dumps({k: v for k, v in cat["units"].items()})
    is_temp = cat_key == "temperature"

    if is_temp:
        tool_js = f"""
const UNITS = {units_js};
const TEMP_FORMULAS = {{
  to_celsius: {{'Celsius': v=>v, 'Fahrenheit': v=>(v-32)*5/9, 'Kelvin': v=>v-273.15}},
  from_celsius: {{'Celsius': v=>v, 'Fahrenheit': v=>v*9/5+32, 'Kelvin': v=>v+273.15}}
}};
function convert(){{
  const v=parseFloat(document.getElementById('input').value);
  if(isNaN(v)){{document.getElementById('error').classList.add('show');document.getElementById('result').classList.remove('show');return}}
  document.getElementById('error').classList.remove('show');
  const from=document.getElementById('from-unit').value;
  const to=document.getElementById('to-unit').value;
  const c=TEMP_FORMULAS.to_celsius[from](v);
  const r=TEMP_FORMULAS.from_celsius[to](c);
  document.getElementById('result-value').textContent=r.toLocaleString('en-US',{{maximumFractionDigits:6}});
  document.getElementById('result').classList.add('show');
}}
"""
    else:
        tool_js = f"""
const FACTORS = {units_js};
function convert(){{
  const v=parseFloat(document.getElementById('input').value);
  if(isNaN(v)){{document.getElementById('error').classList.add('show');document.getElementById('result').classList.remove('show');return}}
  document.getElementById('error').classList.remove('show');
  const from=document.getElementById('from-unit').value;
  const to=document.getElementById('to-unit').value;
  const r=v*FACTORS[from]/FACTORS[to];
  document.getElementById('result-value').textContent=r.toLocaleString('en-US',{{maximumFractionDigits:10}});
  document.getElementById('result').classList.add('show');
}}
"""

    tool_html = f"""
<div class="tool-row">
  <div class="input-group" style="flex:1">
    <label>From</label>
    <input type="number" id="input" placeholder="Enter value..." step="any" autofocus oninput="convert()">
    <select id="from-unit" style="margin-top:8px" onchange="convert()">
      {''.join(f'<option value="{k}">{k}</option>' for k in cat['units'])}
    </select>
  </div>
  <div class="arrow">→</div>
  <div class="input-group" style="flex:1">
    <label>To</label>
    <input type="text" id="output-display" readonly style="font-weight:600;font-size:1.2rem">
    <select id="to-unit" style="margin-top:8px" onchange="convert()">
      {''.join(f'<option value="{k}">{k}</option>' for k in list(cat['units'].keys())[1:])}
    </select>
  </div>
</div>
<div class="error-msg" id="error">Please enter a valid number</div>
<div class="result-box" id="result">
  <div class="label">Result</div>
  <div class="value" id="result-value"></div>
</div>
"""
    tool_js = tool_js.replace(
        "document.getElementById('result').classList.add('show');",
        "document.getElementById('result').classList.add('show');document.getElementById('output-display').value=document.getElementById('result-value').textContent;"
    )

    info_html = f"""
<h2>About {title}</h2>
<p>{desc} This converter supports all major units and performs instant calculations in your browser.</p>
<h2>Available units</h2>
<ul>{''.join(f'<li>{k}</li>' for k in cat['units'])}</ul>
<p>Use the converter above to switch between any two units. The conversion is performed instantly as you type.</p>
"""

    related = []
    for (f, t) in cat["pairs"]:
        r_slug = f"{slugify(unit_full(f))}-to-{slugify(unit_full(t))}.html"
        related.append({"url": r_slug, "title": f"{unit_full(f)} to {unit_full(t)}"})
    related = related[:8]

    return make_page(title, desc, slug, cat["title"], f"{cat['title'].lower()}, {cat_key} converter, convert {cat_key}", cat["title"], tool_html, tool_js, info_html, related, all_tools_js)

# ============================================================
# INDEX PAGE
# ============================================================

def make_index_page(all_tools, categories):
    """Generate the homepage with all tools listed by category."""
    cat_sections = ""
    for cat_name, tools in categories.items():
        cat_slug = slugify(cat_name)
        tool_links = "".join(
            f'<a href="{t["url"]}">{t["title"]}</a>' for t in tools
        )
        cat_sections += f"""
    <div id="category-{cat_slug}">
      <h2>{cat_name}</h2>
      <div class="related-grid">{tool_links}</div>
    </div>"""

    all_tools_js = json.dumps([{"title": t["title"], "url": t["url"], "keywords": t.get("keywords", "")} for t in all_tools])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ToolHub — Free Online Tools | Converters, Calculators, Developer Tools</title>
<meta name="description" content="Free online tools: unit converters, developer tools, text tools, calculators, color tools. Fast, accurate, no signup. All tools run in your browser.">
<meta name="keywords" content="online tools, free tools, converter, calculator, developer tools, text tools, color tools">
<meta property="og:title" content="ToolHub — Free Online Tools">
<meta property="og:description" content="Free online tools: unit converters, developer tools, text tools, calculators, color tools. Fast, accurate, no signup.">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}/">
<link rel="canonical" href="{SITE_URL}/">
<link rel="stylesheet" href="/static/style.css">
</head>
<body>
<header>
  <div class="header-inner">
    <a href="/" class="logo">Tool<span>Hub</span></a>
    <div class="search-bar">
      <input type="text" placeholder="Search 100+ tools..." id="search-input">
      <div class="search-results" id="search-results"></div>
    </div>
  </div>
</header>
<div class="container">
  <div style="padding:32px 0">
    <h1>Free Online Tools</h1>
    <p class="subtitle">{len(all_tools)}+ tools — unit converters, developer tools, text tools, calculators and more. All free, all in your browser.</p>
  </div>
  <div class="ad-slot"></div>
  {cat_sections}
  <div class="ad-slot"></div>
</div>
<footer>
  <p>ToolHub &mdash; Free Online Tools</p>
  <p>&copy; 2026 ToolHub. All tools run in your browser. No data sent to servers.</p>
</footer>
<script src="/static/app.js"></script>
<script>window.ALL_TOOLS = {all_tools_js};</script>
</body>
</html>"""

# ============================================================
# SITEMAP & ROBOTS
# ============================================================

def make_sitemap(pages):
    urls = "".join(f"""
  <url>
    <loc>{SITE_URL}/{p}</loc>
    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{'1.0' if p == 'index.html' else '0.8'}</priority>
  </url>""" for p in pages)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}
</urlset>"""

ROBOTS_TXT = f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
"""

# ============================================================
# VERCEL CONFIG
# ============================================================

VERCEL_JSON = """{
  "version": 2,
  "builds": [{"src": "package.json", "use": "@vercel/static-build"}],
  "routes": [
    {"src": "/", "dest": "/index.html"},
    {"src": "/static/(.*)", "dest": "/static/$1"}
  ]
}
"""

# ============================================================
# MAIN BUILD
# ============================================================

def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.join(OUT, "static"), exist_ok=True)

    # Copy static files
    import shutil
    static_src = os.path.join(os.path.dirname(__file__), "static")
    static_dst = os.path.join(OUT, "static")
    if os.path.exists(static_dst):
        shutil.rmtree(static_dst)
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dst)

    all_tools = []
    all_pages = []
    categories = {}

    # Build all_tools_js for search (will be embedded in each page)
    # First pass: collect all tool metadata
    tool_meta = []

    # Converter category pages
    for cat_key, cat in CONVERTERS.items():
        cat_slug = slugify(cat["title"])
        tool_meta.append({
            "title": cat["title"],
            "url": f"{cat_slug}.html",
            "keywords": cat["title"].lower() + ", " + cat_key + " converter"
        })

    # Converter pair pages
    for cat_key, cat in CONVERTERS.items():
        for (from_u, to_u) in cat["pairs"]:
            slug = f"{slugify(unit_full(from_u))}-to-{slugify(unit_full(to_u))}"
            tool_meta.append({
                "title": f"{unit_full(from_u)} to {unit_full(to_u)}",
                "url": f"{slug}.html",
                "keywords": f"{unit_full(from_u)} to {unit_full(to_u)}, convert {unit_full(from_u).lower()}"
            })

    # Unique tools
    for tool in UNIQUE_TOOLS:
        tool_meta.append({
            "title": tool["title"],
            "url": f"{tool['slug']}.html",
            "keywords": tool.get("keywords", "")
        })

    all_tools_js = json.dumps(tool_meta)

    # Generate converter category pages
    for cat_key, cat in CONVERTERS.items():
        page = make_converter_category_page(cat_key, cat, all_tools_js)
        slug = slugify(cat["title"])
        path = os.path.join(OUT, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        all_pages.append(f"{slug}.html")
        all_tools.append({"title": cat["title"], "url": f"{slug}.html", "keywords": cat["title"]})
        categories.setdefault(cat["title"], []).append({"title": cat["title"], "url": f"{slug}.html"})

    # Generate converter pair pages
    for cat_key, cat in CONVERTERS.items():
        for (from_u, to_u) in cat["pairs"]:
            page = make_converter_pair_page(cat_key, cat, from_u, to_u, all_tools_js)
            slug = f"{slugify(unit_full(from_u))}-to-{slugify(unit_full(to_u))}"
            path = os.path.join(OUT, f"{slug}.html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(page)
            all_pages.append(f"{slug}.html")
            all_tools.append({"title": f"{unit_full(from_u)} to {unit_full(to_u)}", "url": f"{slug}.html", "keywords": f"{unit_full(from_u)} to {unit_full(to_u)}"})
            categories.setdefault(cat["title"], []).append({"title": f"{unit_full(from_u)} to {unit_full(to_u)}", "url": f"{slug}.html"})

    # Generate unique tool pages
    for tool in UNIQUE_TOOLS:
        info_html = f"""
<h2>About {tool['title']}</h2>
<p>{tool['desc']}</p>
<p>This tool runs entirely in your browser. Your data is never sent to any server, ensuring complete privacy and security.</p>
"""
        # Find related tools in same category
        related = []
        for t in UNIQUE_TOOLS:
            if t["slug"] != tool["slug"] and t["category"] == tool["category"]:
                related.append({"url": f"{t['slug']}.html", "title": t["title"]})
            if len(related) >= 8:
                break

        page = make_page(
            tool["title"], tool["desc"], tool["slug"], tool["category"],
            tool.get("keywords", ""), tool["category"],
            tool["html"], tool["js"], info_html, related, all_tools_js
        )
        path = os.path.join(OUT, f"{tool['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        all_pages.append(f"{tool['slug']}.html")
        all_tools.append({"title": tool["title"], "url": f"{tool['slug']}.html", "keywords": tool.get("keywords", "")})
        categories.setdefault(tool["category"], []).append({"title": tool["title"], "url": f"{tool['slug']}.html"})

    # Generate index page
    index_html = make_index_page(all_tools, categories)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    all_pages.append("index.html")

    # Generate sitemap
    sitemap = make_sitemap(all_pages)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    # Generate robots.txt
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(ROBOTS_TXT)

    # Generate vercel.json
    with open(os.path.join(OUT, "..", "vercel.json"), "w", encoding="utf-8") as f:
        f.write(VERCEL_JSON)

    # Generate package.json for Vercel
    pkg = {"name": "toolhub", "version": "1.0.0", "scripts": {"build": "python build.py"}}
    with open(os.path.join(os.path.dirname(__file__), "package.json"), "w") as f:
        json.dump(pkg, f)

    print(f"Build complete! {len(all_pages)} pages generated in {OUT}")
    print(f"Categories: {', '.join(categories.keys())}")
    print(f"Tools: {len(all_tools)}")

if __name__ == "__main__":
    main()
