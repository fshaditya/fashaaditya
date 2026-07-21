/**
 * INDUSTRIAL SKEUOMORPHISM / REALISM INTERACTION ENGINE
 * Fasha Aditya Febrianto Portfolio - Teknik Industri ITENAS '25
 */

document.addEventListener('DOMContentLoaded', () => {
  initNoiseOverlay();
  initClock();
  initCopyEmail();
  initTactilePhysics();
  initDeviceTerminal();
});

/**
 * Procedural Micro-Texture Noise Overlay
 */
function initNoiseOverlay() {
  let canvas = document.getElementById('noiseCanvas');
  if (!canvas) {
    canvas = document.createElement('canvas');
    canvas.id = 'noiseCanvas';
    document.body.appendChild(canvas);
  }

  const ctx = canvas.getContext('2d');
  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  function generateNoise() {
    const imgData = ctx.createImageData(width, height);
    const buffer = new Uint32Array(imgData.data.buffer);
    const len = buffer.length;

    for (let i = 0; i < len; i++) {
      if (Math.random() < 0.15) {
        const value = Math.floor(Math.random() * 255);
        buffer[i] = (255 << 24) | (value << 16) | (value << 8) | value;
      }
    }
    ctx.putImageData(imgData, 0, 0);
  }

  generateNoise();

  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      generateNoise();
    }, 200);
  });
}

/**
 * Live Monospaced Uptime Clock
 */
function initClock() {
  const clockEl = document.getElementById('liveClock');
  if (!clockEl) return;

  function update() {
    const now = new Date();
    const hrs = String(now.getHours()).padStart(2, '0');
    const mins = String(now.getMinutes()).padStart(2, '0');
    const secs = String(now.getSeconds()).padStart(2, '0');
    clockEl.textContent = `${hrs}:${mins}:${secs} WIB`;
  }

  update();
  setInterval(update, 1000);
}

/**
 * Copy Email with Industrial Toast Notification
 */
function initCopyEmail() {
  const btn = document.getElementById('btnCopyEmail');
  const emailStr = 'fshaditya@gmail.com';

  if (!btn) return;

  btn.addEventListener('click', () => {
    navigator.clipboard.writeText(emailStr).then(() => {
      showToast('EMAIL COPIED: ' + emailStr);
    }).catch(() => {
      const input = document.createElement('input');
      input.value = emailStr;
      document.body.appendChild(input);
      input.select();
      document.execCommand('copy');
      document.body.removeChild(input);
      showToast('EMAIL COPIED: ' + emailStr);
    });
  });
}

function showToast(message) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    document.body.appendChild(toast);
  }

  toast.innerHTML = `
    <span class="led-dot" style="width:8px; height:8px; display:inline-block;"></span>
    <span>${message}</span>
  `;

  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
}

/**
 * Mechanical Tactile Physics for Buttons
 */
function initTactilePhysics() {
  const buttons = document.querySelectorAll('.btn, .dial, .project-card, .data-well');

  buttons.forEach(el => {
    el.addEventListener('mousedown', () => {
      el.classList.add('pressed');
    });
    el.addEventListener('mouseup', () => {
      el.classList.remove('pressed');
    });
    el.addEventListener('mouseleave', () => {
      el.classList.remove('pressed');
    });
  });
}

/**
 * Hero Device Terminal Mode Switcher
 */
function initDeviceTerminal() {
  const screenContent = document.getElementById('deviceScreenContent');
  const dial = document.getElementById('deviceDial');
  if (!screenContent || !dial) return;

  const screens = [
    `
      <div class="screen-line accent">&gt; STUDENT: FASHA ADITYA FEBRIANTO</div>
      <div class="screen-line">&gt; MAJOR: TEKNIK INDUSTRI</div>
      <div class="screen-line">&gt; CAMPUS: ITENAS BANDUNG</div>
      <div class="screen-line muted">&gt; BATCH: ANGKATAN 2025</div>
      <div class="screen-line accent" style="margin-top: 10px;">&gt; STATUS: ACTIVE STUDENT [OPERATIONAL]</div>
    `,
    `
      <div class="screen-line accent">&gt; FOCUS AREAS LOG:</div>
      <div class="screen-line">&gt; 01. MANUFACTURING SYSTEM DESIGN</div>
      <div class="screen-line">&gt; 02. ERGONOMICS & WORK STUDY</div>
      <div class="screen-line">&gt; 03. SUPPLY CHAIN & INVENTORY</div>
      <div class="screen-line muted">&gt; 04. INDUSTRIAL QUALITY CONTROL</div>
    `,
    `
      <div class="screen-line accent">&gt; ACADEMIC & SKILLS METRICS:</div>
      <div class="screen-line">&gt; SYSTEM ANALYSIS : 92%</div>
      <div class="screen-line">&gt; WORK STUDY & RULA : 90%</div>
      <div class="screen-line">&gt; PLANT LAYOUT DESIGN : 88%</div>
      <div class="screen-line muted">&gt; BATCH YEAR : 2025 (ITENAS)</div>
    `
  ];

  let currentIndex = 0;

  dial.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % screens.length;
    screenContent.innerHTML = screens[currentIndex];
    dial.style.transform = `rotate(${currentIndex * 120}deg)`;
  });
}
