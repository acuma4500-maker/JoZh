// Oyun listesi (yalnızca meta veri; oyun kodu ihtiyaç anında yüklenir).
export const GAMES = [
  { id: 'xox', name: 'XOX', emoji: '❌', tagline: 'Klasik 3x3, sıra sende!', color: 'rose', module: () => import('./xox.js') },
  { id: 'know-me', name: 'Birbirimizi Ne Kadar Tanıyoruz?', emoji: '💞', tagline: 'Gizli cevaplar, büyük yüzleşme', color: 'peach', module: () => import('./know-me.js') },
  { id: 'truth-dare', name: 'Doğruluk mu Cesaret mi?', emoji: '🎲', tagline: 'Romantik, eğlenceli, saygılı', color: 'plum', module: () => import('./truth-dare.js') },
  { id: 'emoji', name: 'Emojiyle Anlat', emoji: '🤔', tagline: 'Sadece emojilerle anlat, tahmin etsin', color: 'sun', module: () => import('./emoji.js') },
  { id: 'memory', name: 'Hafıza Oyunu', emoji: '🃏', tagline: 'Aynı tahta, sırayla eşleştir', color: 'mint', module: () => import('./memory.js') },
  { id: 'story', name: 'Birlikte Hikâye', emoji: '📜', tagline: 'Sırayla birer cümle', color: 'sky', module: () => import('./story.js') },
  { id: 'questions', name: 'Soru Cevap', emoji: '💬', tagline: '400 soru, iki cevap', color: 'lilac', module: () => import('./questions.js') },
];
export const gameById = (id) => GAMES.find((g) => g.id === id);
