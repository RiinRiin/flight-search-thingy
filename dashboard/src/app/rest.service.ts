import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Flights } from './flights';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http:HttpClient) { }

  url: string = "http://localhost:5000/api";
  getFlights(){
    return this.http.get<Flights[]>(this.url + "/flights");
  }

  getStations(station){
    return this.http.get<Flights[]>(this.url + "/" + station);
  }
}
