// Uygulamaya ait sabit SVG ikonları (kullanıcı verisi içermez). stroke = currentColor.
const s = (body, vb = '0 0 24 24') => `<svg viewBox="${vb}" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">${body}</svg>`;

export const icons = {
  home: s('<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V9.5"/>'),
  chat: s('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.6A8 8 0 1 1 21 12Z"/><path d="M9.2 10.3c0-1 .8-1.7 1.7-1.7.5 0 .9.2 1.1.6.3-.4.7-.6 1.2-.6 1 0 1.7.8 1.7 1.7 0 1.9-2.9 3.4-2.9 3.4s-2.8-1.5-2.8-3.4Z"/>'),
  book: s('<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5v-15Z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/><path d="M12 7.6c-.4-.5-1-.8-1.6-.8-1.1 0-1.9.9-1.9 1.9 0 2 3.5 3.8 3.5 3.8s3.5-1.8 3.5-3.8c0-1-.8-1.9-1.9-1.9-.6 0-1.2.3-1.6.8Z"/>'),
  film: s('<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M7 4v16M17 4v16M3 9h4M17 9h4M3 15h4M17 15h4"/>'),
  check: s('<path d="m5 12.5 4.5 4.5L19 7.5"/>'),
  checks: s('<path d="m2.5 12.5 4.5 4.5 9-9.5"/><path d="m11 16 1 1 9-9.5"/>'),
  tasks: s('<rect x="3.5" y="3.5" width="17" height="17" rx="4"/><path d="m8 12 3 3 5-6"/>'),
  lock: s('<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/><circle cx="12" cy="15.5" r="1.4"/>'),
  unlock: s('<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 7.6-1.7"/><circle cx="12" cy="15.5" r="1.4"/>'),
  game: s('<path d="M7 8h10a5 5 0 0 1 4.8 6.4l-.7 2.4a2.6 2.6 0 0 1-4.4 1L14.5 15.5h-5L7.3 17.8a2.6 2.6 0 0 1-4.4-1l-.7-2.4A5 5 0 0 1 7 8Z"/><path d="M8 11v3M6.5 12.5h3"/><circle cx="16" cy="11.5" r=".6" fill="currentColor"/><circle cx="17.5" cy="13.5" r=".6" fill="currentColor"/>'),
  user: s('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>'),
  bell: s('<path d="M6 16V11a6 6 0 1 1 12 0v5l1.5 2h-15L6 16Z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>'),
  plus: s('<path d="M12 5v14M5 12h14"/>'),
  edit: s('<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16v4Z"/><path d="m13.5 6.5 4 4"/>'),
  trash: s('<path d="M4 7h16M10 11v6M14 11v6"/><path d="M6 7l1 12.5A1.6 1.6 0 0 0 8.6 21h6.8a1.6 1.6 0 0 0 1.6-1.5L18 7"/><path d="M9 7V4.5h6V7"/>'),
  send: s('<path d="M21 3 10 14"/><path d="m21 3-6.5 18-4-8-8-4L21 3Z"/>'),
  back: s('<path d="M15 5l-7 7 7 7"/>'),
  close: s('<path d="M6 6l12 12M18 6 6 18"/>'),
  logout: s('<path d="M15 4h3a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-3"/><path d="M10 16l-4-4 4-4M6 12h10"/>'),
  star: s('<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9L12 3.5Z"/>'),
  heart: s('<path d="M12 20.5s-8-4.6-8-10.6A4.6 4.6 0 0 1 12 7a4.6 4.6 0 0 1 8 2.9c0 6-8 10.6-8 10.6Z"/>'),
  clock: s('<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>'),
  menu: s('<path d="M4 7h16M4 12h16M4 17h10"/>'),
  sparkles: s('<path d="M12 3.5 13.6 9l5.4 1.6-5.4 1.6L12 17.7l-1.6-5.5L5 10.6 10.4 9 12 3.5Z"/><path d="M19 16v4M17 18h4"/>'),
  wifiOff: s('<path d="M3 3l18 18"/><path d="M8.5 16.4a5 5 0 0 1 6.3-.5M5 12.9a10 10 0 0 1 4.2-2.5M2 9.3A15 15 0 0 1 6.4 6.6M14.6 10.3A10 10 0 0 1 19 12.9M11 5.1A15 15 0 0 1 22 9.3"/><circle cx="12" cy="19.5" r=".8" fill="currentColor"/>'),
  smile: s('<circle cx="12" cy="12" r="8.5"/><path d="M8.5 14.5a4.5 4.5 0 0 0 7 0"/><circle cx="9" cy="10" r=".7" fill="currentColor"/><circle cx="15" cy="10" r=".7" fill="currentColor"/>'),
  eye: s('<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/>'),
  shield: s('<path d="M12 3 4.5 6v5.5c0 4.5 3.2 8.2 7.5 9.5 4.3-1.3 7.5-5 7.5-9.5V6L12 3Z"/><path d="m9 12 2 2 4-4"/>'),
  refresh: s('<path d="M20 11a8 8 0 0 0-14.3-4.5L4 8.5"/><path d="M4 4v4.5h4.5"/><path d="M4 13a8 8 0 0 0 14.3 4.5l1.7-2"/><path d="M20 20v-4.5h-4.5"/>'),
  calendar: s('<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'),
  flag: s('<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>'),
  dice: s('<rect x="3.5" y="3.5" width="17" height="17" rx="4"/><circle cx="8.5" cy="8.5" r="1" fill="currentColor"/><circle cx="15.5" cy="15.5" r="1" fill="currentColor"/><circle cx="12" cy="12" r="1" fill="currentColor"/>'),
  backspace: s('<path d="M8.5 5H20a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H8.5L3 12l5.5-7Z"/><path d="m11 9.5 5 5M16 9.5l-5 5"/>'),
};

export const logoSvg = `<svg viewBox="0 0 64 64" width="64" height="64" aria-hidden="true" focusable="false">
  <defs><linearGradient id="lg-box" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F2A9BB"/><stop offset="1" stop-color="#B85C75"/></linearGradient></defs>
  <path d="M10 28h44v24a5 5 0 0 1-5 5H15a5 5 0 0 1-5-5V28Z" fill="url(#lg-box)"/>
  <rect x="7" y="20" width="50" height="10" rx="4" fill="#762F48"/>
  <rect x="29" y="20" width="6" height="37" fill="#FFF0E6" opacity=".85"/>
  <path d="M32 19c-2.6-5.4-9.8-7.4-11.8-3.6-1.7 3.3 3.6 4.8 11.8 3.6Zm0 0c2.6-5.4 9.8-7.4 11.8-3.6 1.7 3.3-3.6 4.8-11.8 3.6Z" fill="#E88FA5" stroke="#762F48" stroke-width="1.6"/>
  <path d="M32 47.5s-7-4-7-8.8a3.8 3.8 0 0 1 7-2.1 3.8 3.8 0 0 1 7 2.1c0 4.8-7 8.8-7 8.8Z" fill="#FFF8F6"/>
</svg>`;
