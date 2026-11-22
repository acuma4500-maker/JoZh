// Testler için sahte YouTube IFrame Player API (gerçek YouTube'a erişilemeyen ortamda eşleşme mantığını sınamak için).
window.YT = {
  PlayerState: { UNSTARTED: -1, ENDED: 0, PLAYING: 1, PAUSED: 2, BUFFERING: 3, CUED: 5 },
  Player: class {
    constructor(el, opts) {
      this.opts = opts; this.vid = opts.videoId || ''; this.state = -1; this.base = 0; this.t0 = 0;
      window.__yt = this;
      const f = document.createElement('div');
      f.className = 'fake-yt'; f.textContent = `▶ ${this.vid}`; f.style.cssText = 'color:#fff;display:grid;place-items:center;height:100%';
      (typeof el === 'string' ? document.getElementById(el) : el).replaceWith(f);
      this.el = f;
      setTimeout(() => opts.events?.onReady?.({ target: this }), 30);
    }
    _emit(s) { this.state = s; this.opts.events?.onStateChange?.({ data: s, target: this }); }
    cueVideoById(a) { this.vid = typeof a === 'object' ? a.videoId : a; this.base = (typeof a === 'object' && a.startSeconds) || 0; this.el.textContent = `▶ ${this.vid}`; this._emit(5); }
    playVideo() { if (this.state === 1) return; this.t0 = performance.now(); this._emit(1); }
    pauseVideo() { if (this.state !== 1) return; this.base = this.getCurrentTime(); this._emit(2); }
    seekTo(t) { this.base = t; if (this.state === 1) this.t0 = performance.now(); }
    getCurrentTime() { return this.state === 1 ? this.base + (performance.now() - this.t0) / 1000 : this.base; }
    getPlayerState() { return this.state; }
    getDuration() { return 600; }
    mute() { this.muted = true; }
    unMute() { this.muted = false; }
    isMuted() { return !!this.muted; }
    getVideoData() { return { video_id: this.vid, title: `Test videosu ${this.vid}` }; }
    destroy() { this.el?.remove(); if (window.__yt === this) window.__yt = null; }
  },
};
