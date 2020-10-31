#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/stat.h>

int main( int argc, char **argv ) {
	char	path[256] = "/proc/";
	DIR		*dir = NULL;

	struct dirent	*entry,*entry_sub;

	if( (dir=opendir(path)) == NULL ) {
		printf( "Fail to open specified directory!" );
		return -1;
	}
	else {
		while( entry=readdir(dir) ) {
			//printf( "filename = %s",entry->d_name );
			if( isdigit(entry->d_name) ) {
				//strcat(path,entry->d_name);
				printf( "%s\n", path );
				// print( "%s\n", strcat(path,entry->d_name) );
				/*
				while( entry_sub=readdir( strcat(path,entry->d_name) ) ) {
					printf( "filename=%s",entry->d_name );
					printf( "\n" );
				}
				*/
			}

			//printf( "filetype = %d",entry->d_type );
			printf( "\n" );
		}
		closedir( dir );
	}
	return 0;
}
