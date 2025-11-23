// API Configuration
// Temporarily hardcoded for production deployment
const API_URL = import.meta.env.VITE_API_URL || '/api';

console.log('🔧 API_URL configured as:', API_URL);
console.log('🔧 VITE_API_URL env var:', import.meta.env.VITE_API_URL);

export default API_URL;
