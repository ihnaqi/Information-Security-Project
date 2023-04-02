import { Component, OnInit } from '@angular/core';
import { AppointmentService } from 'src/app/services/appointment.service';
import { ActivatedRoute, Router } from '@angular/router';

import { Doctor} from 'src/app/models/doctor.model';
import { DoctorService } from 'src/app/services/doctor.service';
import { Appointment } from 'src/app/models/appointment.model';

@Component({
  selector: 'app-appointment-details',
  templateUrl: './appointments-details.component.html',
  styleUrls: ['./appointments-details.component.css']
})

export class AppointmentsDetailsComponent implements OnInit {
  
  status : any = "4";
  currentAppointment: Appointment = {
    appointment_id: '',
    // appointment_amount: 0,
    patient:'',
    doctor:'',
    appointment_time:'',
    
  };
  message = '';
  doctors?: Doctor[];
  constructor(
    private appointmentService: AppointmentService,
    private doctorService: DoctorService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.retrieveDoctors();
      this.getAppointment(this.route.snapshot.params.id);
    }
    
    
  retrieveDoctors(): void {
    this.doctorService.getAll()
      .subscribe(
        data => {
          this.doctors = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

    getAppointment(id: string): void {
      this.appointmentService.get(id)
        .subscribe(
          data => {
            this.currentAppointment = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        appointment_id: this.currentAppointment.appointment_id,
        // appointment_amount: 0,
        appointment_time:'',
        doctor:'',
      };
  
      this.message = '';
  
      this.appointmentService.update(this.currentAppointment.appointment_id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updateAppointment(): void {
  
      this.appointmentService.update(this.currentAppointment.appointment_id, this.currentAppointment)
        .subscribe(
            
          error => {
            console.log(error);
          });
        this.router.navigate(['/View-Doctors/'+this.currentAppointment.patient]);
          
    }
  
    deleteAppointment(): void {
      this.appointmentService.delete(this.currentAppointment.appointment_id)
        .subscribe(
          response => {
       
            this.message = response.message ? response.message : 'This appointment was deleted successfully!';
            this.router.navigate(['/View-Doctors/'+this.currentAppointment.patient]);
          },
          error => {
            console.log(error);
          });
    }
  }

