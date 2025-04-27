const accessKey = 'TU_ACCESS_KEY_DE_UNSPLASH';

export async function fetchPhoneImage(phoneModel) {
  const response = await fetch(`https://api.unsplash.com/search/photos?query=${encodeURIComponent(phoneModel)}&client_id=${accessKey}&per_page=1`);
  const data = await response.json();

  if (data.results && data.results.length > 0) {
    return data.results[0].urls.small;
  } else {
    return 'https://via.placeholder.com/300x300?text=Imagen+no+disponible';
  }
}
