// Arayüzde gösterilen Türkçe adlar: türler, durumlar ve alan adları.

export const STORE_LABELS = {
  profile: 'Profil',
  partner: 'Sevdiğim kadın',
  settings: 'Ayarlar',
  memories: 'Anı',
  diary: 'Günlük',
  dreams: 'Hedef',
  plans: 'Plan',
  notes: 'Not',
  transactions: 'Gelir/gider'
};

export const BLOOD_TYPES = ['A Rh+', 'A Rh−', 'B Rh+', 'B Rh−', 'AB Rh+', 'AB Rh−', '0 Rh+', '0 Rh−'];

export const PRIORITIES = { low: 'Düşük', medium: 'Orta', high: 'Yüksek' };
export const PRIORITY_ORDER = { high: 0, medium: 1, low: 2 };

export const DREAM_STATUS = {
  notStarted: 'Başlanmadı',
  inProgress: 'Devam ediyor',
  completed: 'Tamamlandı',
  postponed: 'Ertelendi'
};

export const DREAM_CATEGORIES = ['Kariyer', 'Eğitim', 'Sağlık', 'Spor', 'Seyahat', 'Para', 'İlişki', 'Aile', 'Ev', 'Hobi', 'Kişisel gelişim'];

export const PLAN_TYPES = {
  trip: 'Seyahat',
  date: 'Buluşma',
  work: 'İş',
  personal: 'Kişisel',
  special: 'Özel gün',
  other: 'Diğer'
};

export const PLAN_STATUS = { planned: 'Planlandı', completed: 'Tamamlandı', cancelled: 'İptal' };

export const VAULT_TYPES = {
  note: 'Özel not',
  thought: 'Kişisel düşünce',
  diary: 'Özel günlük',
  photos: 'Fotoğraflar',
  surprise: 'Sürpriz planı',
  memory: 'Özel hatıra'
};

export const TXN_TYPES = { income: 'Gelir', expense: 'Gider' };

export const TXN_ACCOUNTS = { cash: 'Nakit', bank: 'Banka', card: 'Kredi kartı' };

// Başlangıç bakiyesi aylık gelire sayılmaz; yalnızca bakiyeyi başlatır.
export const OPENING_CATEGORY = 'Başlangıç bakiyesi';

export const INCOME_CATEGORIES = ['Maaş', 'Ek iş', 'Prim', 'Kira geliri', 'Satış', 'Hediye', 'Borç geri ödemesi', 'Diğer gelir'];

export const EXPENSE_CATEGORIES = [
  'Market', 'Yemek', 'Kira', 'Faturalar', 'Ulaşım', 'Yakıt', 'Sağlık', 'Giyim', 'Eğlence',
  'Eğitim', 'Abonelikler', 'Hediye', 'Ev', 'Kredi / borç', 'Kart ödemesi', 'Diğer gider'
];

export const FIELD_LABELS = {
  common: { deleted: 'Silinmiş', title: 'Başlık', tags: 'Etiketler', date: 'Tarih', notes: 'Notlar', photoId: 'Fotoğraf', photoIds: 'Fotoğraflar', description: 'Açıklama' },
  profile: {
    firstName: 'Ad', lastName: 'Soyad', birthDate: 'Doğum tarihi', bloodType: 'Kan grubu', height: 'Boy',
    weight: 'Kilo', phone: 'Telefon', about: 'Hakkımda', photoId: 'Profil fotoğrafı'
  },
  notes: { title: 'Başlık', body: 'Metin', tags: 'Etiketler', pinned: 'Sabitleme' },
  diary: { title: 'Başlık', date: 'Tarih', body: 'Metin', tags: 'Etiketler', photoIds: 'Fotoğraflar' },
  dreams: {
    title: 'Başlık', description: 'Açıklama', category: 'Kategori', targetDate: 'Hedef tarihi', priority: 'Öncelik',
    progress: 'İlerleme', status: 'Durum', notes: 'Notlar', photoId: 'Fotoğraf'
  },
  plans: {
    name: 'Ad', type: 'Tür', status: 'Durum', startDate: 'Başlangıç tarihi', startTime: 'Başlangıç saati',
    endDate: 'Bitiş tarihi', endTime: 'Bitiş saati', location: 'Konum', description: 'Açıklama', budget: 'Bütçe',
    spent: 'Harcama', checklist: 'Hazırlık listesi', notes: 'Notlar', trip: 'Seyahat bilgileri'
  },
  memories: { title: 'Başlık', date: 'Tarih', description: 'Açıklama', tags: 'Etiketler', photoIds: 'Fotoğraflar' },
  partner: {
    name: 'Ad', nickname: 'Hitap', birthDate: 'Doğum tarihi', togetherSince: 'Birlikte olunan tarih', summary: 'Kısa tanım',
    photoId: 'Fotoğraf', traits: 'Kişilik özellikleri', likes: 'Sevdikleri', dislikes: 'Sevmedikleri', foods: 'Sevdiği yemekler',
    colors: 'Renkler', perfumes: 'Parfümler', hobbies: 'Hobiler', importantDates: 'Önemli tarihler', todos: 'Birlikte yapılacaklar',
    surprises: 'Sürpriz fikirleri', privateNotes: 'Özel notlar'
  },
  settings: { calendarView: 'Takvim görünümü' },
  transactions: { type: 'Tür', amount: 'Tutar', category: 'Kategori', date: 'Tarih', account: 'Hesap', note: 'Açıklama' }
};

export function fieldLabel(store, field) {
  return (FIELD_LABELS[store] && FIELD_LABELS[store][field]) || FIELD_LABELS.common[field] || field;
}

// Bir kaydın listelerde ve çakışma ekranında gösterilecek adı.
export function recordTitle(store, record) {
  if (!record) return STORE_LABELS[store] || store;
  switch (store) {
    case 'profile': return 'Profilim';
    case 'partner': return 'Sevdiğim kadın';
    case 'settings': return 'Ayarlar';
    case 'plans': return record.name || 'Adsız plan';
    case 'notes': return record.title || (record.body ? String(record.body).slice(0, 40) : 'Adsız not');
    case 'transactions': return `${TXN_TYPES[record.type] || ''} · ${record.category || ''}`;
    default: return record.title || 'Adsız kayıt';
  }
}
