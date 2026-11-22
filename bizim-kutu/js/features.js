// Adım adım yayın: hangi bölümlerin açık olduğu burada belirlenir.
// Bir bölümü açmadan önce ona ait Firebase kuralları yüklenmiş olmalı (firebase/adimlar/ klasörü).
// Giriş (PIN), Ana sayfa ve Profil her zaman açıktır.
export const FEATURES = Object.freeze({
  chat: true,           // Sohbet (2. adım)
  memories: true,       // Anı defteri (3. adım)
  movies: true,         // Film & dizi (5. adım)
  tasks: true,          // Yapılacaklar (4. adım)
  vault: true,          // Özel kasa (8. adım)
  games: true,          // Oyun merkezi (7 oyun) (7. adım)
  notifications: true,  // Bildirimler (6. adım)
  watch: true,          // Birlikte izle (9. adım)
});
export const on = (name) => !name || FEATURES[name] === true;
