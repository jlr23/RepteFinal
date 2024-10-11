import axios from "axios";

const locations = axios.create({ 
  baseURL: "https://retoolapi.dev/YFhjbG",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  }
});

const osm = axios.create({ 
  baseURL: "https://nominatim.openstreetmap.org/search",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  }
});

export default {
  getAllLocations() {
    return locations.get("/locations");
  },
  getLocationById(id) {
    return locations.get(`/locations/${id}`);
  },
  createLocation(location) {
    return locations.post("/locations", location);
  },
  updateLocation(id, location) {
    return locations.put(`/locations/${id}`, location);
  },
  deleteLocation(id) {
    return locations.delete(`/locations/${id}`);
  },
  searchLocationOSM(query) {
    const data = {
      params: {
        q: query,
        format: 'json',
        addressdetails: 1,
      }
    }
    return osm.get(data);
  }
}