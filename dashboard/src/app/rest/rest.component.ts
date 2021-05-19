import { Component, OnInit } from '@angular/core';
import { Flights } from '../flights';
import { RestService } from '../rest.service';

@Component({
  selector: 'app-rest',
  templateUrl: './rest.component.html',
  styleUrls: ['./rest.component.css']
})
export class RestComponent implements OnInit {

  displayedColumns: string[] = [
    'id', 
    'created_at', 
    'updated_at', 
    'flight_identifier', 
    'flt_num', 
    'scheduled_origin_gate', 
    'scheduled_destination_gate', 
    'out_gmt', 
    'in_gmt', 
    'off_gmt', 
    'on_gmt', 
    'destination', 
    'origin', 
    'destination_full_name', 
    'origin_full_name'
  ];

  flights: Flights[] = [];

  constructor(public rs:RestService) {  }

  ngOnInit(): void {
    this.rs.getFlights().subscribe((res) => {
      this.flights = res;
    })
  }

  applyFilter(event: Event) {
    let filterValue = (event.target as HTMLInputElement).value;
    if (filterValue.length == 0){
      this.rs.getFlights().subscribe((res) => {
        this.flights = res;
      })
    } else {
      this.rs.getStations(filterValue).subscribe((res) => {
        this.flights = res;
      })
    }
  }

}
