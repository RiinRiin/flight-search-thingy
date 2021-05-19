import { Component, OnInit } from '@angular/core';
import { Flights } from '../flights';
import { RestService } from '../rest.service';

@Component({
  selector: 'app-rest',
  templateUrl: './rest.component.html',
  styleUrls: ['./rest.component.css']
})
export class RestComponent implements OnInit {
  flights: Flights[] = [];

  constructor(public rs:RestService) { }

  ngOnInit(): void {
    this.rs.getFlights().subscribe((res) => {
      this.flights = res;
      console.log(this.flights[0][291451])
    })
  }

}
