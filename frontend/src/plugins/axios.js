// axios
import axios from 'axios'
import Vue from 'vue'

const axiosIns = axios.create({
  // You can add your headers here
  // ================================
  // baseURL: 'http://localhost:8000/',
  withCredentials: true
  // timeout: 1000,
  // headers: {'X-Custom-Header': 'foobar'}
})

function getCookie(name) {
  console.log(decodeURIComponent(document.cookie))
  if (!document.cookie) {
    return null;  
  }
  console.log(document.cookie.split(';'))
  const xsrfCookies = document.cookie.split(';')
    .map(c => c.trim())
    .filter(c => c.startsWith(name + '='));

  if (xsrfCookies.length === 0) {
    return null;
  }
  return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

axiosIns.interceptors.request.use(function (config) {
  var csrfToken = getCookie('csrftoken');
   config.headers['X-CSRFToken'] =  csrfToken;
  return config;
});

// axiosIns.interceptors.request.use(
//   config => {
//     // Do something before request is sent

//     const accessToken = localStorage.getItem('accessToken')

//     // eslint-disable-next-line no-param-reassign
//     if (accessToken) config.headers.Authorization = `Bearer ${accessToken}`

//     return config
//   },
//   error => Promise.reject(error),
// )

Vue.prototype.$http = axiosIns

export default axiosIns