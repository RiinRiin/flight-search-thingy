export class Flights {
    id: string;
    created_at: string;
    updated_at: string;
    flight_identifier: string;
    flt_num: string;
    scheduled_origin_gate: string;
    scheduled_destination_gate: string;
    out_gmt: string;
    in_gmt: string;
    off_gmt: string;
    on_gmt: string;
    destination: string;
    origin: string;
    destination_full_name: string;
    origin_full_name: string;

    constructor(id, created_at, updated_at, flight_identifier, flt_num, scheduled_origin_gate, scheduled_destination_gate, out_gmt, in_gmt, off_gmt, on_gmt, destination, origin, destination_full_name, origin_full_name){
        this.id=id;
        this.created_at=created_at;
        this.updated_at=updated_at;
        this.flight_identifier=flight_identifier;
        this.flt_num=flt_num;
        this.scheduled_origin_gate=scheduled_origin_gate;
        this.scheduled_destination_gate=scheduled_destination_gate;
        this.out_gmt=out_gmt;
        this.in_gmt=in_gmt;
        this.off_gmt=off_gmt;
        this.on_gmt=on_gmt;
        this.destination=destination;
        this.origin=origin;
        this.destination_full_name=destination_full_name;
        this.origin_full_name=origin_full_name;
    }
}
