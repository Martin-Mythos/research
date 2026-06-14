export const siteContent = {
  shop: 'Talking Breads Tervuren',
  positioning: 'Greek-inspired burgers, sandwiches, salads, fries & takeaway',
  notice: 'Official V1 discovery site concept — no online ordering or payment.',
  contact: { phone: '+32 000 00 00 00', mapsUrl: 'https://maps.google.com/?q=Talking+Breads+Tervuren', instagramUrl: 'https://instagram.com/talkingbreads', email: 'info@talkingbreads.be (placeholder, not verified)' },
  promotions: [{ title: 'Student lunch offer', time: '12:00-14:00', text: 'Seasonal/changeable offer; confirm in-store before ordering.' }],
  hours: [
    { season: 'Summer', rows: ['Mon-Fri 11:30-21:00', 'Sat-Sun 12:00-21:30'] },
    { season: 'September/October placeholder', rows: ['Schedule may change after summer; update this data file when confirmed.'] }
  ],
  allergens: ['gluten', 'milk', 'egg', 'sesame', 'nuts', 'soy'],
  menu: [
    { category: 'Burgers', name: 'Greek Smash Burger', price: '€12 sample', allergens: ['gluten','milk'], photo: false },
    { category: 'Burgers', name: 'Halloumi Burger', price: '€11 sample', allergens: ['gluten','milk','sesame'], photo: false },
    { category: 'Sandwiches', name: 'Chicken Gyros Sandwich', price: '€9 sample', allergens: ['gluten','milk'], photo: false },
    { category: 'Sandwiches', name: 'Falafel Pita', price: '€8 sample', allergens: ['gluten','sesame'], photo: false },
    { category: 'Salads', name: 'Greek Village Salad', price: '€10 sample', allergens: ['milk'], photo: false },
    { category: 'Starters', name: 'Tzatziki & Pita', price: '€6 sample', allergens: ['gluten','milk'], photo: false },
    { category: 'Fries', name: 'Feta Oregano Fries', price: '€5 sample', allergens: ['milk'], photo: false },
    { category: 'Drinks', name: 'Homemade Lemonade', price: '€4 sample', allergens: [], photo: false }
  ]
} as const;
