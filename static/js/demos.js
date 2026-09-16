/* ----------------------------------------------------
   Interactive Project Demos Controller - demos.js
   ---------------------------------------------------- */

document.addEventListener('DOMContentLoaded', () => {
  // Modal Controller Setup
  const modalOverlay = document.getElementById('demo-modal-overlay');
  const modalContainer = document.getElementById('demo-modal-container');
  const modalTitle = document.getElementById('demo-modal-title');
  const modalBody = document.getElementById('demo-modal-body');
  const modalCloseBtn = document.getElementById('demo-modal-close');

  const demoLaunchBtns = document.querySelectorAll('.launch-demo-btn');

  demoLaunchBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const demoType = btn.getAttribute('data-demo');
      openDemoModal(demoType);
    });
  });

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeDemoModal);
  }

  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeDemoModal();
    });
  }

  function closeDemoModal() {
    if (modalOverlay) modalOverlay.classList.remove('active');
  }

  function openDemoModal(demoType) {
    if (!modalOverlay || !modalBody) return;
    
    modalBody.innerHTML = '';
    modalOverlay.classList.add('active');

    if (demoType === 'fraud-detection') {
      modalTitle.innerHTML = `<i data-lucide="shield-alert"></i> Credit Card Fraud Detection ML Playground`;
      renderFraudDetectionDemo();
    } else if (demoType === 'sales-analytics') {
      modalTitle.innerHTML = `<i data-lucide="line-chart"></i> Power BI Sales Analytics & Profitability Explorer`;
      renderSalesAnalyticsDemo();
    } else if (demoType === 'interview-coach') {
      modalTitle.innerHTML = `<i data-lucide="bot"></i> AI Mock Interview Coach & Scorer`;
      renderInterviewCoachDemo();
    }

    if (window.lucide) lucide.createIcons();
  }


  /* ==================================================
     DEMO 1: Credit Card Fraud Detection Simulator
     ================================================== */
  function renderFraudDetectionDemo() {
    modalBody.innerHTML = `
      <div class="demo-grid-2col">
        <!-- Input Controls -->
        <div class="demo-panel">
          <div class="demo-panel-title"><i data-lucide="sliders"></i> Transaction Feature Inputs</div>
          
          <div class="range-slider-group">
            <div class="slider-header">
              <span>Transaction Amount ($)</span>
              <span class="slider-val" id="amt-val">$1,250.00</span>
            </div>
            <input type="range" id="amt-slider" min="10" max="5000" step="10" value="1250">
          </div>

          <div class="range-slider-group">
            <div class="slider-header">
              <span>Time of Day (24h)</span>
              <span class="slider-val" id="time-val">03:00 AM (Night)</span>
            </div>
            <input type="range" id="time-slider" min="0" max="23" step="1" value="3">
          </div>

          <div class="range-slider-group">
            <div class="slider-header">
              <span>PCA Anomaly Vector V1</span>
              <span class="slider-val" id="v1-val">-1.50</span>
            </div>
            <input type="range" id="v1-slider" min="-5.0" max="5.0" step="0.1" value="-1.5">
          </div>

          <div class="range-slider-group">
            <div class="slider-header">
              <span>PCA Anomaly Vector V2</span>
              <span class="slider-val" id="v2-val">2.10</span>
            </div>
            <input type="range" id="v2-slider" min="-5.0" max="5.0" step="0.1" value="2.1">
          </div>

          <div class="switch-group">
            <span>Cross-Border / International IP</span>
            <input type="checkbox" id="intl-switch" checked style="width:20px; height:20px;">
          </div>

          <button id="run-fraud-btn" class="btn btn-primary" style="width:100%; justify-content:center; margin-top:1rem;">
            <i data-lucide="zap"></i> Run ML Fraud Predictor Engine
          </button>
        </div>

        <!-- Output Analytics -->
        <div class="demo-panel" id="fraud-result-panel">
          <div class="demo-panel-title"><i data-lucide="cpu"></i> XGBoost ML Prediction Result</div>
          <div class="risk-gauge-box">
            <div style="font-size:0.9rem; color:var(--text-muted);">Fraud Risk Score</div>
            <div id="fraud-score-num" style="font-size:2.8rem; font-weight:800; color:var(--accent-rose);">78.4%</div>
            <div class="risk-meter">
              <div id="fraud-meter-fill" class="risk-meter-fill" style="width: 78.4%;"></div>
            </div>
            <div id="fraud-badge" class="decision-badge fraud">DECLINE & FLAG</div>
          </div>

          <div style="font-size:0.85rem; background:rgba(0,0,0,0.3); padding:0.8rem; border-radius:8px; margin-bottom:1rem;">
            <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
              <span>Model Architecture:</span> <strong style="color:var(--accent-cyan)">XGBoost + FastAPI</strong>
            </div>
            <div style="display:flex; justify-content:space-between;">
              <span>Inference Latency:</span> <strong id="latency-val" style="color:var(--accent-emerald)">4.2 ms</strong>
            </div>
          </div>

          <div style="font-weight:700; font-size:0.9rem; margin-bottom:0.4rem;">Risk Factors Detected:</div>
          <ul id="risk-factors-list" style="font-size:0.85rem; padding-left:1.2rem; color:var(--text-muted);">
            <li>High Transaction Value ($1,250.00) exceeds standard threshold</li>
            <li>Unusual Transaction Hour (03:00 AM) off-peak time</li>
            <li>Cross-border / International IP location flagged</li>
          </ul>
        </div>
      </div>
    `;

    // Bind event listeners
    const amtSlider = document.getElementById('amt-slider');
    const timeSlider = document.getElementById('time-slider');
    const v1Slider = document.getElementById('v1-slider');
    const v2Slider = document.getElementById('v2-slider');
    const intlSwitch = document.getElementById('intl-switch');
    const runBtn = document.getElementById('run-fraud-btn');

    amtSlider.addEventListener('input', (e) => {
      document.getElementById('amt-val').textContent = `$${parseFloat(e.target.value).toLocaleString('en-US', {minimumFractionDigits:2})}`;
      triggerFraudAPI();
    });

    timeSlider.addEventListener('input', (e) => {
      const h = parseInt(e.target.value);
      const ampm = h >= 12 ? 'PM' : 'AM';
      const displayHour = h % 12 === 0 ? 12 : h % 12;
      document.getElementById('time-val').textContent = `${displayHour.toString().padStart(2, '0')}:00 ${ampm} ${h >= 1 && h <= 4 ? '(Night)' : ''}`;
      triggerFraudAPI();
    });

    v1Slider.addEventListener('input', (e) => {
      document.getElementById('v1-val').textContent = parseFloat(e.target.value).toFixed(2);
      triggerFraudAPI();
    });

    v2Slider.addEventListener('input', (e) => {
      document.getElementById('v2-val').textContent = parseFloat(e.target.value).toFixed(2);
      triggerFraudAPI();
    });

    intlSwitch.addEventListener('change', triggerFraudAPI);
    runBtn.addEventListener('click', triggerFraudAPI);

    // Initial Trigger
    triggerFraudAPI();
  }

  async function triggerFraudAPI() {
    const payload = {
      amount: parseFloat(document.getElementById('amt-slider').value),
      transaction_time: parseInt(document.getElementById('time-slider').value),
      v1_feature: parseFloat(document.getElementById('v1-slider').value),
      v2_feature: parseFloat(document.getElementById('v2-slider').value),
      is_international: document.getElementById('intl-switch').checked
    };

    try {
      const res = await fetch('/api/demo/fraud-detection', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      if (res.ok && data.status === 'success') {
        updateFraudUI(data);
      }
    } catch (err) {
      console.error('Fraud API error', err);
    }
  }

  function updateFraudUI(data) {
    const scoreNum = document.getElementById('fraud-score-num');
    const meterFill = document.getElementById('fraud-meter-fill');
    const badge = document.getElementById('fraud-badge');
    const latencyVal = document.getElementById('latency-val');
    const factorsList = document.getElementById('risk-factors-list');

    const prob = data.prediction.fraud_probability;
    scoreNum.textContent = `${prob}%`;
    meterFill.style.width = `${prob}%`;

    if (data.prediction.is_fraudulent) {
      scoreNum.style.color = 'var(--accent-rose)';
      badge.className = 'decision-badge fraud';
      badge.textContent = data.prediction.decision;
    } else {
      scoreNum.style.color = 'var(--accent-emerald)';
      badge.className = 'decision-badge legit';
      badge.textContent = data.prediction.decision;
    }

    latencyVal.textContent = `${data.performance_metrics.inference_time_ms} ms`;
    factorsList.innerHTML = data.risk_factors.map(rf => `<li>${rf}</li>`).join('');
  }


  /* ==================================================
     DEMO 2: Sales Analytics & Power BI Chart Playground
     ================================================== */
  let salesChart1 = null;
  let salesChart2 = null;

  async function renderSalesAnalyticsDemo() {
    modalBody.innerHTML = `
      <div class="kpi-cards-row">
        <div class="kpi-mini-card">
          <div class="kpi-mini-val" id="kpi-rev">$1,485,200</div>
          <div class="kpi-mini-lbl">Total Sales Revenue</div>
        </div>
        <div class="kpi-mini-card">
          <div class="kpi-mini-val" style="color:var(--accent-emerald)" id="kpi-margin">21.3%</div>
          <div class="kpi-mini-lbl">Optimized Margin</div>
        </div>
        <div class="kpi-mini-card">
          <div class="kpi-mini-val" style="color:var(--primary)" id="kpi-boost">+15.1% Uplift</div>
          <div class="kpi-mini-lbl">Profit Margin Boost</div>
        </div>
        <div class="kpi-mini-card">
          <div class="kpi-mini-val" id="kpi-orders">14,250</div>
          <div class="kpi-mini-lbl">Orders Processed</div>
        </div>
      </div>

      <div class="charts-grid-2col">
        <div class="demo-panel">
          <div class="demo-panel-title"><i data-lucide="bar-chart-2"></i> Monthly Sales & Profit Margin Uplift</div>
          <div class="chart-container">
            <canvas id="monthlySalesChart"></canvas>
          </div>
        </div>
        <div class="demo-panel">
          <div class="demo-panel-title"><i data-lucide="pie-chart"></i> Regional Sales Share</div>
          <div class="chart-container">
            <canvas id="regionalSalesChart"></canvas>
          </div>
        </div>
      </div>

      <div class="demo-panel">
        <div class="demo-panel-title"><i data-lucide="lightbulb"></i> Power BI DAX & Analytics Insights</div>
        <ul id="insights-list" style="font-size:0.9rem; padding-left:1.2rem; color:var(--text-muted);">
          <li>Loading interactive insights...</li>
        </ul>
      </div>
    `;

    try {
      const res = await fetch('/api/demo/sales-analytics');
      const data = await res.json();
      initSalesCharts(data);
    } catch (err) {
      console.error('Sales analytics error', err);
    }
  }

  function initSalesCharts(data) {
    // Populate Insights
    const list = document.getElementById('insights-list');
    if (list && data.key_insights) {
      list.innerHTML = data.key_insights.map(i => `<li style="margin-bottom:6px;">${i}</li>`).join('');
    }

    // Chart 1: Monthly Sales & Margin
    const ctx1 = document.getElementById('monthlySalesChart').getContext('2d');
    if (salesChart1) salesChart1.destroy();

    salesChart1 = new Chart(ctx1, {
      type: 'line',
      data: {
        labels: data.monthly_performance.map(m => m.month),
        datasets: [
          {
            label: 'Optimized Margin % (After DAX Insights)',
            data: data.monthly_performance.map(m => m.optimized_margin),
            borderColor: '#10b981',
            backgroundColor: 'rgba(16, 185, 129, 0.1)',
            borderWidth: 3,
            fill: true,
            tension: 0.3
          },
          {
            label: 'Baseline Margin % (Before)',
            data: data.monthly_performance.map(m => m.profit_margin),
            borderColor: '#64748b',
            borderDash: [5, 5],
            borderWidth: 2,
            fill: false,
            tension: 0.1
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { labels: { color: '#94a3b8' } }
        },
        scales: {
          x: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' } },
          y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' } }
        }
      }
    });

    // Chart 2: Regional Pie Chart
    const ctx2 = document.getElementById('regionalSalesChart').getContext('2d');
    if (salesChart2) salesChart2.destroy();

    salesChart2 = new Chart(ctx2, {
      type: 'doughnut',
      data: {
        labels: data.regional_breakdown.map(r => r.region),
        datasets: [{
          data: data.regional_breakdown.map(r => r.sales),
          backgroundColor: data.regional_breakdown.map(r => r.color),
          borderWidth: 2,
          borderColor: '#0f172a'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { position: 'bottom', labels: { color: '#94a3b8' } }
        }
      }
    });
  }


  /* ==================================================
     DEMO 3: AI Interview Coach & Scoring Sandbox
     ================================================== */
  async function renderInterviewCoachDemo() {
    modalBody.innerHTML = `
      <div class="demo-grid-2col">
        <!-- Controls -->
        <div class="demo-panel">
          <div class="demo-panel-title"><i data-lucide="user-check"></i> Candidate Role & Question</div>
          
          <div class="form-group" style="margin-bottom:1rem;">
            <label>Select Targeted Tech Role</label>
            <select id="ai-role-select" class="form-control">
              <option value="Data Scientist" selected>Data Scientist</option>
              <option value="Data Analyst">Data Analyst</option>
              <option value="Python Developer">Python Developer</option>
            </select>
          </div>

          <div class="form-group" style="margin-bottom:1rem;">
            <label>Select Mock Interview Question</label>
            <select id="ai-q-select" class="form-control"></select>
          </div>

          <div class="form-group" style="margin-bottom:1rem;">
            <label>Your Candidate Answer (Text / Speech Transcript)</label>
            <textarea id="ai-user-ans" class="form-control" style="min-height:110px;" placeholder="Type your technical response here..."></textarea>
          </div>

          <button id="submit-ai-ans-btn" class="btn btn-primary" style="width:100%; justify-content:center;">
            <i data-lucide="sparkles"></i> Evaluate Response with AI Engine
          </button>
        </div>

        <!-- Feedback Result -->
        <div class="demo-panel">
          <div class="demo-panel-title"><i data-lucide="award"></i> AI Evaluation & Vector Score</div>
          
          <div class="ai-score-ring" style="--score-pct: 88;">
            <div class="ai-score-inner">
              <div class="ai-score-num" id="ai-overall-num">88</div>
              <div style="font-size:0.65rem; color:var(--text-muted);">OVERALL</div>
            </div>
          </div>
          <div id="ai-grade-badge" style="text-align:center; font-weight:800; color:var(--accent-emerald); margin-bottom:1rem;">EXCELLENT RESPONSE</div>

          <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:0.8rem;">
            <div>Semantic Vector Match: <strong id="ai-vector-match" style="color:var(--accent-cyan)">86%</strong> (Chroma DB)</div>
          </div>

          <div style="font-weight:700; font-size:0.88rem; margin-bottom:0.4rem;">AI Feedback & Suggestions:</div>
          <ul id="ai-feedback-list" style="font-size:0.84rem; padding-left:1.2rem; color:var(--text-muted); margin-bottom:1rem;">
            <li>Great inclusion of key technical concepts!</li>
          </ul>

          <div style="font-weight:700; font-size:0.88rem; margin-bottom:0.4rem;">Vector Retrieved Ideal Answer:</div>
          <div id="ai-ideal-sample" style="font-size:0.82rem; background:rgba(0,0,0,0.4); padding:0.8rem; border-radius:8px; color:#a7f3d0; border:1px solid rgba(16,185,129,0.3);">
            Loading ideal response...
          </div>
        </div>
      </div>
    `;

    const roleSelect = document.getElementById('ai-role-select');
    const qSelect = document.getElementById('ai-q-select');
    const submitBtn = document.getElementById('submit-ai-ans-btn');

    roleSelect.addEventListener('change', () => loadQuestions(roleSelect.value));
    submitBtn.addEventListener('click', submitInterviewAPI);

    await loadQuestions(roleSelect.value);
  }

  let currentQuestionsPool = [];

  async function loadQuestions(role) {
    try {
      const res = await fetch(`/api/demo/interview-questions?role=${encodeURIComponent(role)}`);
      const data = await res.json();
      currentQuestionsPool = data.questions || [];
      
      const qSelect = document.getElementById('ai-q-select');
      const ansText = document.getElementById('ai-user-ans');

      if (qSelect && currentQuestionsPool.length > 0) {
        qSelect.innerHTML = currentQuestionsPool.map(q => `<option value="${q.id}">${q.question}</option>`).join('');
        ansText.value = currentQuestionsPool[0].ideal_sample;
      }
    } catch (err) {
      console.error('Load questions error', err);
    }
  }

  async function submitInterviewAPI() {
    const role = document.getElementById('ai-role-select').value;
    const qId = document.getElementById('ai-q-select').value;
    const userAns = document.getElementById('ai-user-ans').value;
    
    const targetQ = currentQuestionsPool.find(q => q.id === qId);

    const payload = {
      role: role,
      question_id: qId,
      question_text: targetQ ? targetQ.question : "Technical Question",
      user_response: userAns
    };

    try {
      const res = await fetch('/api/demo/interview-coach', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      if (res.ok && data.status === 'success') {
        updateInterviewUI(data);
      }
    } catch (err) {
      console.error('Interview API error', err);
    }
  }

  function updateInterviewUI(data) {
    const evalData = data.evaluation;
    const scoreNum = document.getElementById('ai-overall-num');
    const gradeBadge = document.getElementById('ai-grade-badge');
    const vectorMatch = document.getElementById('ai-vector-match');
    const feedbackList = document.getElementById('ai-feedback-list');
    const idealSample = document.getElementById('ai-ideal-sample');

    scoreNum.textContent = evalData.overall_score;
    gradeBadge.textContent = evalData.grade;
    vectorMatch.textContent = evalData.vector_similarity_match;

    feedbackList.innerHTML = evalData.feedback.map(fb => `<li>${fb}</li>`).join('');
    idealSample.textContent = evalData.sample_recommended_answer;
  }
});
