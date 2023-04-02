import { NgModule } from '@angular/core';
import { MatToolbarModule } from "@angular/material/toolbar";
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { NgxPaginationModule } from 'ngx-pagination';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NavbarComponent } from './components/navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SummaryComponent } from './components/summary/summary.component';
import { CashflowsComponent } from './components/cashflows/cashflows.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { DoctorsListComponent } from './components/doctors-list/doctors-list.component';
import { AddAppointmentsComponent } from './components/add-appointments/add-appointments.component';
import { AppointmentsDetailsComponent } from './components/appointments-details/appointments-details.component';
import { AppointmentsListComponent } from './components/appointments-list/appointments-list.component';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    SummaryComponent,
    CashflowsComponent,
    SidebarComponent,
    DoctorsListComponent,
    AddAppointmentsComponent,
    AppointmentsDetailsComponent,
    AppointmentsListComponent,
  ],

  exports: [
    NavbarComponent,
  ],

  imports: [
    
    MatToolbarModule,
    NgxPaginationModule,
    AppRoutingModule,
    RouterModule,
    BrowserModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule { }
